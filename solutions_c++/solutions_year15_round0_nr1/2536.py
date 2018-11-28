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



int main(int argc, char **argv){
    ifs.open("A-large.in");
    ofs.open("A-large.out");
    
	int T = 0;
    ifs >> T;

	rep(i, T){
        ofs << "Case #" << i + 1 << ": ";

        int S_max = 0;
        ifs >> S_max;

        int* S = new int[S_max + 1];
        rep(j, S_max + 1){
            char c;
            ifs >> c;
            S[j] = c - '0';
        }

        int sum = S[0];
        int numToInvite = 0;
        for(int j = 1; j <= S_max; j++){
            if(j > numToInvite + sum){
                numToInvite = j - sum;
            }
            sum += S[j];
        }

        ofs << numToInvite << endl;
	}
	

    ifs.close();
    ofs.close();
    return 0;
}
