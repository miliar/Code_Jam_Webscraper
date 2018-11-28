#include <iostream>
#include <cstdio>
#include <vector>
#include <set>
using namespace std;
typedef pair<double, int> P;
int T;
int N;
const int MAX_N = 1005;
bool used_k[MAX_N];
bool used[2*MAX_N];
int main(int argc, const char * argv[])
{
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        scanf("%d", &N);
        bool ken_has_one = false;
        bool naomi_has_zero = false;
        vector<P> v;
        for (int i = 0; i < N; i++) {
            double d;
            scanf("%lf", &d);
            if (d == 0.0) naomi_has_zero = true;
            v.push_back(P(d, i));
        }
        for (int i = 0; i < N; i++) {
            double d;
            scanf("%lf", &d);
            if (d == 1.0) ken_has_one = true;
            v.push_back(P(d, i+MAX_N));
        }
        sort(v.begin(), v.end());
        vector<int> Naomi;
        vector<int> Ken;
        for (int i = 0; i < v.size(); i++) {
            if (v[i].second < MAX_N) {
                Naomi.push_back(i+1);
            } else {
                Ken.push_back(i+1);
            }
        }
        memset(used_k, false, sizeof(used_k));
        memset(used, false, sizeof(used));

        //deceitful war
        if (ken_has_one || naomi_has_zero) {
            for (int i = 0; i < 2*N; i++) {
                if (v[i].second < MAX_N) {
                    used[i] = true;
                    break;
                }
            }
            for (int i = 2*N-1; i >= 0; i--) {
                if (v[i].second >= MAX_N) {
                    used[i] = true;
                    break;
                }
            }
        }
        int d_p_n = 0;
        for (int i = 0; i < 2*N; i++) {
            if (!used[i]) {
                if (v[i].second >= MAX_N) {  //Kenの場合
                    for (int j = i+1; j < 2*N; j++) {
                        if (v[j].second < MAX_N && !used[j]) {
                            used[i] = used[j] = true;
                            d_p_n++;
                            break;
                        }
                    }
                } else {  //Naomi
                    for (int j = 2*N-1; j >= 0; j--) {
                        if (v[j].second >= MAX_N && !used[j]) {
                            used[i] = used[j] = true;
                            break;
                        }
                    }
                }
            }
        }
        int p_n = 0;
        int p_k = 0;
        sort(Ken.begin(), Ken.end());
        memset(used_k, false, sizeof(used_k));
        for (int i = 0; i < N; i++) {
            int told_N = Naomi[i];
            int i_k = -1;
            for (int j = 0; j < N; j++) {
                if (used_k[j]) continue;
                if (told_N < Ken[j] && (i_k == -1 || Ken[i_k] > Ken[j])) {
                    i_k = j;
                }
            }
            if (i_k == -1) {  //Naomi gets a point
                for (int j = 0; j < N; j++) {
                    if (!used_k[j]) {
                        used_k[j] = true;
                        break;
                    }
                }
                p_n++;
            } else {
                p_k++;
                used_k[i_k] = true;
            }
        }
        printf("Case #%d: %d %d\n", t+1, d_p_n, p_n);
    }
    return 0;
}

