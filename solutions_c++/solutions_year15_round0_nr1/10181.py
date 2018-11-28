#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <stack>
#include <queue>
#include <unordered_set>
#include <cstdlib>
#include <fstream>

using namespace std;

string s;
int smax,result,sum;
ifstream infile;
ofstream outfile;

void solve(int i){
    infile >> smax >> s;
    result = 0;
    sum = 0;
    sum += (s[0] - '0');
    for (int j=1; j<=smax; j++) {
        if (j > sum){
            result += j - sum;
            sum = s[j]-'0' + j;
        }
        else{
            sum += s[j]-'0';
        }
    }
    
    outfile << "Case #"<< i+1 << ": "<< result <<endl;
}

int main(int argc, const char * argv[]) {
    int T;
    infile.open("A_S.in");
    outfile.open("A_S.out");
        infile >> T;
    for (int i = 0; i < T; i++) {
        solve(i);
    }
    infile.close();
    outfile.close();
    return 0;
}
