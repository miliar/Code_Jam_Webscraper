#include <bits/stdc++.h>
#define ll long long
using namespace std;
ll solve(char s[],int n)
{
    ll pl[n+1], mi[n+1];
    if(s[0]=='+'){
        pl[0]=0;
        mi[0]=1;
    }
    else {
        pl[0]=1;
        mi[0]=0;
    }
    for(int i=1;i<n;i++){
        if(s[i]=='+'){
            pl[i]=min(pl[i-1] , mi[i-1]+1);
            mi[i]=min(pl[i-1]+1, mi[i-1]+2);
        }
        else {
            mi[i]=min(mi[i-1],pl[i-1]+1);
            pl[i]=min(mi[i-1]+1,pl[i-1]+2);
        }
        //cout<<pl[i]<<"   ";
    }
    return pl[n-1];
}
int main()
{
    int t;
    scanf("%d",&t);
    for(int z=1;z<=t;z++){
      char s[110],s1[110];
      scanf("%s",s);
      int n=strlen(s);
      for(int i=n-1;i>=0;i--){
        if(s[i]=='+')
            s1[(n-1)-i]='-';
        else s1[n-i-1]='+';
      }
      s1[n]=NULL;
      ll ans=min(solve(s,n),solve(s1,n)+1);
      printf("Case #%d: %lld\n",z,ans);
    }
    return 0;
}
