#include <iostream>
#include <sstream>
#include <fstream>
#include <climits>
#include <vector>

using namespace std;


vector<int> find_max(int *nums, int N){
    int max = -1;
    for (int i = 0; i < N; i++) {
        if (nums[i] > max){
            max = nums[i];
        }
    }
    vector<int> max_i;
    for (int i = 0; i < N; i++) {
        if (nums[i] == max) {
            max_i.push_back(i);
        }
    }

    return max_i;
}
bool all_zeros(int *nums, int N){
    for (int i = 0; i < N; i++) {
        if (nums[i] != 0) {
            return false;
        }
    }
    return true;
}
int main() {
    ifstream fin;
    fin.open("C:\\Users\\dima6\\ClionProjects\\GoogleCodeJam\\Round1C\\inputA.txt");
    ofstream fout;
    fout.open("C:\\Users\\dima6\\ClionProjects\\GoogleCodeJam\\Round1C\\outputA.txt");
    int T;
    fin >> T;
    for (int k = 1; k <= T; k++) {
        int N;
        fin >> N;
        int *p = new int[N];
        for (int i = 0; i < N; i++) {
            fin >> p[i];
        }
        fout << "Case #" << k << ": ";
        while (all_zeros(p, N) == false) {
            stringstream curr_res;
            vector<int> max_i = find_max(p, N);
            if (p[max_i[0]] == 1) {
                if (max_i.size() % 2 == 0) {
                    for (int i = 0; i < max_i.size(); i += 2) {
                        p[max_i[i]]--;
                        curr_res << (char) ('A' + max_i[i]);
                        if (i + 1 < max_i.size()) {
                            p[max_i[i + 1]]--;
                            curr_res << (char) ('A' + max_i[i + 1]);
                        }
                        curr_res << " ";
                    }
                } else {
                    p[max_i[0]]--;
                    curr_res << (char) ('A' + max_i[0]) << " ";
                    for (int i = 1; i < max_i.size(); i += 2) {
                        p[max_i[i]]--;
                        curr_res << (char) ('A' + max_i[i]);
                        if (i + 1 < max_i.size()) {
                            p[max_i[i + 1]]--;
                            curr_res << (char) ('A' + max_i[i + 1]);
                        }
                        curr_res << " ";
                    }
                }
            } else {
                for (int i = 0; i < max_i.size(); i += 2) {
                    p[max_i[i]]--;
                    curr_res << (char) ('A' + max_i[i]);
                    if (i + 1 < max_i.size()) {
                        p[max_i[i + 1]]--;
                        curr_res << (char) ('A' + max_i[i + 1]);
                    }
                    curr_res << " ";
                }
            }
            fout << curr_res.str();
        }
        fout << endl;
    }

    fin.close();
    fout.close();

    return 0;
}