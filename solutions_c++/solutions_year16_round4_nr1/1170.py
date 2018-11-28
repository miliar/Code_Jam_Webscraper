#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
const int maxn=100000;
const char ch[3]={'P','R','S'};
const int v[3]={1,2,0};

int n,R,P,S;
char st[maxn];

string work(int m,int k)
{
     if(m==0)
     {
        if(k==0) return "P";
        if(k==1) return "R";
        if(k==2) return "S";
     }
     string s1=work(m-1,k);
     string s2=work(m-1,v[k]);
     if(s1+s2<s2+s1) return s1+s2; else return s2+s1;
}

bool check(string s0)
{
     int p=0,r=0,s=0;
     int len=s0.size();
     for(int i=0;i<len;i++)
     {
         if(s0[i]=='P') p++;
         if(s0[i]=='R') r++;
         if(s0[i]=='S') s++;
     }
     if(p!=P || r!=R || s!=S) return false;
     return true;
}

int main()
{
    //freopen("A.in","r",stdin);
    //freopen("A.out","w",stdout);
    int TT=0;
    string s1,s2,s3,ans;
    scanf("%d",&TT);
    for(int i=1;i<=TT;i++)
    {
        printf("Case #%d: ",i);
        scanf("%d %d %d %d",&n,&R,&P,&S);
        ans="IMPOSSIBLE";
        s1=work(n,0);
        if(check(s1) && (s1<ans || ans=="IMPOSSIBLE")) ans=s1;
        s2=work(n,1);
        if(check(s2) && (s2<ans || ans=="IMPOSSIBLE")) ans=s2;
        s3=work(n,2);
        if(check(s3) && (s3<ans || ans=="IMPOSSIBLE")) ans=s3;
        cout<<ans<<endl;
    }
    return 0;
}
