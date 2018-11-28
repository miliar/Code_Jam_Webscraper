#include<cstdio>
#include<algorithm>
#include<iostream>
#include<cstring>
#include<vector>
#include<cmath>
#include<map>
#include<set>
using namespace std;
typedef long long ll;
const int N=12+1;
string s[N][3];
int a[N][3][3];
string work(string st)
{
    if(st.length()==2)return st;
    string s1,s2;
    s1=work(st.substr(0,st.length()/2));
    s2=work(st.substr(st.length()/2,st.length()/2));
    return min(s1,s2)+max(s1,s2);
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int i,j,k;
    memset(a,0,sizeof a);
    s[0][0]="R";a[0][0][0]=1;
    s[0][1]="P";a[0][1][1]=1;
    s[0][2]="S";a[0][2][2]=1;
    for(i=1;i<N;i++)
    {
        for(j=0;j<3;j++)
        {
            for(k=0;k<s[i-1][j].length();k++)
            {
                if(s[i-1][j][k]=='P'){s[i][j]+="PR";a[i][j][0]++;a[i][j][1]++;}
                if(s[i-1][j][k]=='R'){s[i][j]+="RS";a[i][j][0]++;a[i][j][2]++;}
                if(s[i-1][j][k]=='S'){s[i][j]+="PS";a[i][j][2]++;a[i][j][1]++;}
            }
            s[i][j]=work(s[i][j]);
        }
    }
    int t;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        int n,b[3],f=1;
        cin>>n;
        for(i=0;i<3;i++)scanf("%d",b+i);
        printf("Case #%d: ",k);
        for(i=0;i<3;i++)
            if(a[n][i][0]==b[0]&&a[n][i][1]==b[1]&&a[n][i][2]==b[2]){cout<<s[n][i]<<endl;f=0;break;}
        if(f)printf("IMPOSSIBLE\n");
    }
    return 0;
}
