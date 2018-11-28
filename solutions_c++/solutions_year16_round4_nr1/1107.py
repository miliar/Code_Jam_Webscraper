#include <bits/stdc++.h>
using namespace std;
#define LL long long
int s[3][15],p[3][15],r[3][15];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.out","w",stdout);
    string str[3][15],ps="PS",rs="RS",rp="PR";
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
            int gg=str[g][i].size();
            string ss;
            for(int k=4;k<=gg;k<<=1){
                ss="";
                for(int o=0;o<gg;o+=k){
                    string x=str[g][i].substr(o,k/2);
                    string y=str[g][i].substr(o+k/2,k/2);
                    if(x<y) ss+=(x+y);
                    else ss+=(y+x);
                }
                str[g][i]=ss;
            }
        }
        for(int j=0;j<str[g][12].size();j++){
            if(str[g][12][j]=='S') s[g][12]++;
            if(str[g][12][j]=='R') r[g][12]++;
            if(str[g][12][j]=='P') p[g][12]++;
        }
    }
    int t,cas=1;
    scanf("%d",&t);
    while(t--){
        int n,R,P,S;
        scanf("%d%d%d%d",&n,&R,&P,&S);
        int flag=1;
        for(int i=0;i<3;i++){
            if(R==r[i][n]&&S==s[i][n]&&P==p[i][n]){
                printf("Case #%d: ",cas++);
                cout<<str[i][n]<<endl;
                flag=0;
                break;
            }
        }
        if(flag) printf("Case #%d: IMPOSSIBLE\n",cas++);
    }
    return 0;
}
