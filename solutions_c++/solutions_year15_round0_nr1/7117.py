#include <iostream>
#include <fstream>

using namespace std;

int main(){
    ifstream fin("A-large.in");
    ofstream fout("a-big.txt");
    int t, si;
    char s[1010];
    fin>>t;
    int cur;
    int re;
    for (int i = 0; i < t; i++){
        cur = 0;
        re = 0;
        fin>>si>>s;
        cur = s[0] - '0';
        for (int j = 1; j <= si; j++){
            if (s[j] - '0' > 0) {
                if (cur < j){
                    re += j - cur;
                    cur += j - cur + s[j] - '0';
                }
                else
                    cur += s[j] - '0';
            }
            if (cur > si)
                break;
        }
        fout<<"Case #"<<i+1<<": "<<re<<endl;
    }

}
