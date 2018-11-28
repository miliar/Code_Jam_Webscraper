#include <iostream>
#include <string>
#include <fstream>
using namespace std;

ifstream fin("f.in");
ofstream fout("f.out");

int t,n;
char c;

int main() {
    
    fin>>t;
    for (int k = 1; k<=t; k++) {
        fin>>n;
        int sum = 0;
        int result = 0;
        for(int i = 0; i <= n; i++ ) {
            fin >> c;
            int digit = c-'0';
            if(sum<i && digit) {
                result += i-sum;
                sum+=result;
            }
            sum += digit;
        }
        fout << "Case #"<<k<<": "<<result<<'\n';
    }
    fin.close();
    fout.close();
    return 0;
}
