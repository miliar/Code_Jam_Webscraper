#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

int solveWarDeceipt(vector<double>& Naomi, vector<double>& Ken);
int solveWar(vector<double>& Naomi, vector<double>& Ken);

int main() {
    string test_filename;
    cout << "Enter test file : " << endl;
    getline(cin, test_filename);
    cout << endl;

    string out_name = test_filename.substr(0, test_filename.find_last_of(".")) + ".out";
    ifstream in_file(test_filename.c_str());
    ofstream out_file(out_name);

    int T;
    in_file >> T;

    for(int t = 0; t < T; t++) {
        int N;
        in_file >> N;
        vector<double> Naomi(N, 0);
        vector<double> Ken(N, 0);

        for(int i = 0; i < N; i++) {
            in_file >> Naomi[i];
        }
        for(int i = 0; i < N; i++) {
            in_file >> Ken[i];
        }
        std::sort(Naomi.begin(), Naomi.end());
        std::sort(Ken.begin(), Ken.end());

        int score_war = solveWar(Naomi, Ken);
        int score_war_deceipt = solveWarDeceipt(Naomi, Ken);

        out_file << "Case #" << t + 1 << ": " << score_war_deceipt << " " << score_war << endl;
    }
    out_file.close();
}

int solveWarDeceipt(vector<double>& Naomi, vector<double>& Ken) {
    int n_remaining = Naomi.size();
    int N_min = 0, K_min = 0, N_max = Naomi.size() - 1, K_max = Ken.size() - 1;
    int N_score = 0;
    while(K_min <= K_max && N_min <= N_max) {
        if(Naomi[N_min] < Ken[K_min]) {
            N_min++;
            K_max--;
            n_remaining--;
        }
        else {
            N_score++;
            N_min++;
            K_min++;
            n_remaining--;
        }
    }

    return N_score;

}

int solveWar(vector<double>& Naomi, vector<double>& Ken) {
    size_t i = 0, j = 0;
    size_t K_score = 0;
    while(i < Naomi.size() && j < Ken.size()) {
        if(Naomi[i] > Ken[j]) {
            j++;
        }
        else {
            i++;
            j++;
            K_score++;
        }
    }

    return Naomi.size()  - K_score;
}

#if 0
int solveWar(vector<double>& Naomi, vector<double>& Ken) {
    
    int ken_score = 0;
    int naomi_score = 0;

    size_t current_ken = 0;
    for(size_t i = 0; i < Naomi.size(); i++) {
        while(current_ken < Ken.size()) {
            if(Ken[current_ken] > Naomi[i]) {
                ken_score++;
                current_ken++;
                break;
            }
            else {
                current_ken++;
            }
        }
    }

  return Naomi.size() - ken_score;
}
#endif
