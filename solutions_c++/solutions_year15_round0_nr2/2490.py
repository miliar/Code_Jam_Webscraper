#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <vector>
#include <map>
#include <string>
#include <algorithm>
#include <utility>
#include <functional>

#define rep(i,n) for(int i=0;i<n;i++)

using namespace std;


ifstream ifs;
ofstream ofs;
string buf;


int table[1001][1001];


int main(int argc, char **argv){
    rep(i, 1001){
        rep(j, 1001){
            if(i <= j || j == 0){
                table[j][i] = 0;
            }
            else{
                int min = 10000;
                for(int k = 1; k < i; k++){
                    int count = 1 + table[j][k] + table[j][i - k];
                    if(min > count){
                        min = count;
                    }
                }
                table[j][i] = min;
            }
        }
    }
    
    ifs.open("B-large.in");
    ofs.open("B-large.out");
    
	int T = 0;
    ifs >> T;

	rep(i, T){
        ofs << "Case #" << i + 1 << ": ";

        int D = 0;
        ifs >> D;

        int* P = new int[D];
        rep(j, D){
            ifs >> P[j];
        }

        int min = 10000;
        for(int j = 1; j <= 1000; j++){
            int sum = j;
            rep(k, D){
                sum += table[j][P[k]];
            }
            if(min > sum){
                min = sum;
            }
        }

        ofs << min << endl;

        delete[] P;
	}
	

    ifs.close();
    ofs.close();
    return 0;
}
