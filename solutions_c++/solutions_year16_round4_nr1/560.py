#include <bits/stdc++.h>
using namespace std;
#define LL long long
int s[3][15],p[3][15],r[3][15];
string solve(string s){
    int n=s.size();
    string ss;
    for(int k=4;k<=n;k<<=1){
        ss="";
        for(int i=0;i<n;i+=k){
            string x=s.substr(i,k/2);
            string y=s.substr(i+k/2,k/2);
            if(x<y) ss+=(x+y);
            else ss+=(y+x);
        }
        s=ss;
    }
    return s;
}
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
    string str[3][15],ps="PS",rs="RS",rp="PR";
    memset(s,0,sizeof s);
    memset(p,0,sizeof p);
    memset(r,0,sizeof r);
    str[0][0]="R";
    str[1][0]="P";
    str[2][0]="S";
    for(int g=0;g<3;g++){
        for(int i=1;i<=12;i++){
            str[g][i]="";
            for(int j=0;j<str[g][i-1].size();j++){
                if(str[g][i-1][j]=='S') str[g][i]+=ps,s[g][i-1]++;
                if(str[g][i-1][j]=='R') str[g][i]+=rs,r[g][i-1]++;
                if(str[g][i-1][j]=='P') str[g][i]+=rp,p[g][i-1]++;
            }
            str[g][i]=solve(str[g][i]);
        }
        for(int j=0;j<str[g][12].size();j++){
            if(str[g][12][j]=='S') s[g][12]++;
            if(str[g][12][j]=='R') r[g][12]++;
            if(str[g][12][j]=='P') p[g][12]++;
        }
    }
    int t,cas=1;
    cin>>t;
    while(t--){
        int n,R,P,S;
        cin>>n>>R>>P>>S;
        printf("Case #%d: ",cas++);
        int flag=1;
        for(int i=0;i<3;i++){
            if(R==r[i][n]&&S==s[i][n]&&P==p[i][n]){
                cout<<str[i][n]<<endl;
                flag=0;
                break;
            }
        }
        if(flag) puts("IMPOSSIBLE");
    }
    return 0;
}
