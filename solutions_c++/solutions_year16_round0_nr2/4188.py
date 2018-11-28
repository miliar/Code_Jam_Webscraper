#include <iostream>
#include <fstream>
#include <string>
using namespace std;
ifstream fin("B-large.in");
ofstream fout("answer.txt");
int main(){
    int T;
    fin>>T;
    for(int t=0;t<T;t++){
        string s;
        fin>>s;
        int ans = 0;
        for(int i=1;i<s.length();i++){
            if(s[i-1]!=s[i]){
                ans++;
            }
        }
        if(s[s.length()-1]=='-'){
            ans++;
        }
        fout<<"Case #"<<t+1<<": "<<ans<<endl;
    }
    return 0;
}
