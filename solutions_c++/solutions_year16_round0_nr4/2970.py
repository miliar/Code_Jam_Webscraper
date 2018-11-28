#include <iostream>
#include <fstream>
#include <math.h>
#include <stdlib.h>
#include<algorithm>
#include <vector>

void getPos(unsigned long long int s, int i);

using namespace std;



int main() {
    ifstream fin("D-small-attempt1.in");
    ofstream fout("D-small-attempt1.out");
    int totalCases, K ,C, S;
    fin >> totalCases;
    for(int t = 1; t <= totalCases; t++){

        fin>>K;
        fin>>C;
        fin>>S;
        fout << "Case #" << t << ": ";

//        unsigned long long totalTiles = pow(K, C);
        int minS = K - C + 1;
        if (S < minS){
            fout << "IMPOSSIBLE\n";
        }
        else{
            if (minS <= 0){
                minS = 1;
            }

            if (minS >= K || S >=K){
                for (int i=1; i <= K; i++){
                    fout << i;
                    if (i == K){
                        fout << "\n";
                    }
                    else{
                        fout << " ";
                    }
                }
            }
            else{
                int n = K;
                int r = minS;

                vector<bool> v(n);
                fill(v.begin(), v.end() - n + r, true);
                int multiplyCount = 0;
                do {
                    unsigned long long multiply = 1;
                    for (int i = 0; i < n; ++i) {
                        if (v[i]) {
                            multiply = multiply * (i+1);
                            if (t==5) {
                                std::cout << (i + 1) << " ";
                            }
                        }
                    }
                    fout << multiply;
                    multiplyCount++;
                    if (multiplyCount >= minS){
                        fout << "\n";
                        break;
                    }
                    else{
                        fout << " ";
                    }
                } while (prev_permutation(v.begin(), v.end()));
            }

        }


    }
    fin.close();
    fout.close();
    exit(0);
}


void printCombination() {

}

