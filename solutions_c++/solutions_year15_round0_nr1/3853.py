#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

int main() {
    int T;
    fin>>T;
    for(int z = 1; z <= T; z++) {
    
    int S;
    fin>>S;
    char s[S+1];
    for(int i = 0; i <= S; i++) {
        fin>>s[i];
        s[i] -= '0';
    }
    
    int num = 0;
    int extra = 0;
    
    for(int i = 0; i <= S; i++) {
        if(s[i] > 0) {
            if(num >= i) {
                num += s[i];
            } else {
                extra += i-num;
                num = i;
                num += s[i];
            }                
        }
    }
    
    fout<<"Case #"<<z<<": "<<extra<<endl;
    
//    cout<<endl;

    }
//    system("pause"); 
}
