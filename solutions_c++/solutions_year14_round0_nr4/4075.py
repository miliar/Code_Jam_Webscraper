#include <iostream>
#include <vector>
#include <utility>
#include <fstream>
#include <iomanip>

using namespace std;

int main(int argc, char* argv[])
{
    ifstream input;
    ofstream output;
    
    input.open(argv[1]);
    output.open("output.out");
    
    int T;
    input >> T;
    
    for (int i = 1; i <= T; i++) {
        int num_blocks;
        input >> num_blocks;
        vector<double> N, K;
        for (int i = 0; i < num_blocks; i++) {
            double tmp;
            input >> tmp;
            N.push_back(tmp);
        }
        for (int i = 0; i < num_blocks; i++) {
            double tmp;
            input >> tmp;
            K.push_back(tmp);
        }
        sort(N.begin(), N.end());
        sort(K.begin(), K.end());
        
        int K_head = 0, N_good_win_num = 0;
        for (int i = 0; i < num_blocks; i++) {
            if (N[i] > K[K_head]) {
                N_good_win_num++;
                K_head++;   
            }
        }
        int N_head = 0, K_good_win_num = 0;
        for (int i = 0; i < num_blocks; i++) {
            if (K[i] > N[N_head]) {
                K_good_win_num++;
                N_head++;
            }
        }
        int N_bad_win_num = num_blocks - K_good_win_num;
        
        output << "Case #" << i << ": " << N_good_win_num << " " << N_bad_win_num;
        
        if (i != T)
           output << endl;
    }
}
