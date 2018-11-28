#include<bits/stdc++.h>
using namespace std;

int main(){
    ifstream fin;
    fin.open("B-large.in");
    ofstream fout;
    fout.open("2.txt");
    int j=1;
    int n;
    fin>>n;
    while(n--){
        string s;
        fin>>s;
        int len=s.length();
        int i=len-1,ans=0;
        while(i>=0 and s[i]=='+'){
            i--;
        }
        while(i>=0){
            while(i>=0 and s[i]=='-')
                i--;
            ans++;
            if(i>=0){
                while(i>=0 and s[i]=='+')
                    i--;
                ans++;
            }
        }
        fout<<"Case #"<<j<<": "<<ans<<"\n";
        j++;
    }
    return 0;
}
