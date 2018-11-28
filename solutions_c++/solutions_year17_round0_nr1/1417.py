#include <bits/stdc++.h>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
using namespace std;
ifstream fin("in.in");
ofstream fo("out.out");
int test,n,k,ans=0,ck=0;
string s;
int main(){
    ios_base::sync_with_stdio(0);
    fin>>test;
    for(int t=1;t<=test;t++){
        if(t>1) fo<<"\n";
        fin>>s>>k;
        n=(int) s.length();
        fo<<"Case #"<<t<<": ";
        ck=0;
        ans=0;
        for(int i=0;i<n;i++){
            if(s[i]=='-'){
                if(i+k-1>=n){
                    ck=1;
                    break;
                }
                else{
                    for(int j=i;j<=i+k-1;j++){
                        if(s[j]=='-') s[j]='+';
                        else s[j]='-';
                    }
                    ans++;
                }
            }
            if(ck==1) break;
        }
        if(ck==1) fo<<"IMPOSSIBLE";
        else fo<<ans;
    }
}
