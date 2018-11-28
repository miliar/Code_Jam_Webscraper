#include <bits/stdc++.h>

using namespace std;

char s[1005];

int main(){
    ifstream fin("home.in");
    ofstream fout("home.out");
    int T,test;
    fin>>T;
    for(test = 1;test <= T;test++){
        int n,k,i,j;
        fin>>s + 1;
        n = strlen(s + 1);
        fin>>k;
        bitset <1005> bit(0);
        for(i = 1;i <= n;i++){
            if(s[i] == '+'){
                bit.flip(i);
            }
        }
        int ans = 0;
        for(i = 1;i <= n - k + 1;i++){
            if(bit[i] == 0){
                for(j = i;j <= i + k - 1;j++){
                    bit.flip(j);
                }
                ans++;
            }
        }
        bool ok = true;
        for(i = 1;i <= n;i++){
            ok &= bit[i] == 1;
        }
        fout<<"Case #"<<test<<": ";
        if(ok){
            fout<<ans;
        }else{
            fout<<"IMPOSSIBLE";
        }
        fout<<'\n';
    }
    return 0;
}
