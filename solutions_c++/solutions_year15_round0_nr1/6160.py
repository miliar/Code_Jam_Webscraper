#include <iostream>
#include <string>
#include <fstream>

int n,t;
int s[10000];

using namespace std;

int main() {
    
    ifstream fin ("A-large.in");
    ofstream fout ("A.out");
    
    fin >> t;
    int j = 0;
    while(j < t) {
        j++;
        int cnt = 0;
        int sum;
        string str;
        
        fin >> n;
        fin >> str;
        
        for(int i = 0 ; i <= n ; i++) {
            s[i] = str[i] - '0';
        }
        sum = s[0];
        
        for(int i = 1; i <= n ; i++) {
            if(sum+cnt < i) {
                cnt += i - sum - cnt;
            }
            sum += s[i];
        }
        
        fout << "Case #" << (j) << ": " << cnt << endl;
    }
    
    
}
