#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int cal_ijk(int le, int ri) {
        int sign = 1;

        if (le < 0) {
                sign = sign * (-1);
                le = le * (-1);
        }
        if (ri < 0) {
                sign = sign * (-1);
                ri = ri * (-1);
        }

        if (le == 1)
                return sign * ri;
        if (ri == 1)
                return sign * le;
        if (le == ri)
                return sign * (-1);
        if (le == 'i' && ri == 'j')
                return sign * 'k';
        if (le == 'i' && ri == 'k')
                return (-1) * sign * 'j';
        if (le == 'j' && ri == 'i')
                return (-1) * sign * 'k';
        if (le == 'j' && ri == 'k')
                return sign * 'i';
        if (le == 'k' && ri == 'i')
                return sign * 'j';
        if (le == 'k' && ri == 'j')
                return (-1) * sign * 'i';

        cout << "illege input" << endl;
        return 0;
}

int main() {
        ifstream input;
        ofstream res;
        int T;
        input.open("inputC");
        res.open("outputC");
        input >> T;
        for (int i = 0; i < T; i ++) {
                long long L, X;
                input >> L >> X;
                string dis;
                input >> dis;

                int cal_res = 1;

                for (int j = 0; j < L; j ++) {
                        cal_res = cal_ijk(cal_res, dis[j]);
                }

                int res_ind = X % 4;
                int tot_res = 1;

                for (int j = 0; j < res_ind; j ++) {
                        tot_res = cal_ijk(tot_res, cal_res);
                }

                bool make = false;
                if (tot_res == -1) {
                        int from_end[L];
                        int from_begin[L];
                        int begin = 1;

                        long long begin_min = X * L;
                        for (int j = 0; j < L; j ++) {
                                begin = cal_ijk(begin, dis[j]);
                                from_begin[j] = -1;
                                int temp = 1;
                                for (int k = 0; k < 4; k ++) {
                                        if ('i' == cal_ijk(temp, begin)) {
                                                from_begin[j] = k;
                                                if (begin_min > k * L + j + 1) {
                                                        begin_min = k * L + j + 1;
                                                }
                                                break;
                                        }
                                        temp = cal_ijk(temp, cal_res);
                                }
                        }

                        int end = 1;
                        long long end_min = X * L;

                        for (int j = 0; j < L; j ++) {
                                end = cal_ijk(dis[L - 1 - j], end);
                                from_end[L - 1 - j] = -1;
                                int temp = 1;
                                for (int k = 0; k < 4; k ++) {
                                        if ('k' == cal_ijk(end, temp)) {
                                                from_begin[L - 1 - j] = k;
                                                if (end_min > k * L + j + 1) {
                                                        end_min = k * L + j + 1;
                                                }
                                                break;
                                        }
                                        temp = cal_ijk(temp, cal_res);
                                }
                        }

                        cout << end_min << ", " << begin_min << endl;

                        if (end_min + begin_min < X * L) {
                                make = true;
                        }
                        
                }

                res << "Case #" << i + 1 << ": " << (make ? "YES" : "NO")<< endl;
        }
        input.close();
        res.close();
}
