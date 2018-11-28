#include <bits/stdc++.h>

using namespace std;

long long int give(int x,string g)
{
    long long int ans1,u;
    int i;
    u=1LL;
    ans1=0;
    for(i=g.size()-1;i>=0;i--)
    {
        if(g[i]=='1')
        {
          ans1=ans1+u;
        }
        u=u*x;
    }
    return ans1;
}

int main()
{

    freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
    long long int p,k,u,l,ans[17];
    int flag,j,hua,i,n,h,kl,t;
    hua=0;
    scanf("%d",&t);
    scanf("%d %d",&n,&kl);
    string s;
    string g;
    printf("Case #1:\n");
    p=32769;
while(p<35000){
       s="";
       g="";
    k=p;
    while(k>0)
    {
        if(k%2==0)
            g=g+'0';
        else
            g=g+'1';
        k=k/2;
    }
    for(h=g.size()-1;h>=0;h--)
    {
        s=s+g[h];
    }
   // cout<<s<<"\n";
 memset(ans,0,sizeof(ans));
 for(i=2;i<=10;i++)
 {
     flag=0;
     l=give(i,s);
     if(l%2==0)
     {
         ans[i]=l/2;
         flag=1;
     }
     else
         if(l%3==0)
     {
         ans[i]=l/3;
     flag=1;
     }
     else
      if(l%5==0)
     {
         ans[i]=l/5;
     flag=1;
     }
       else
         if(l%7==0)
     {
         ans[i]=l/7;
     flag=1;
     }
       else
         if(l%11==0)
     {
         ans[i]=l/11;
     flag=1;
     }
     else

         if(l%13==0)
     {
         ans[i]=l/13;
     flag=1;
     }
     if(flag==0)
        break;
 }
 if(flag==0){
  p=p+2;
    continue;
 }
 else{
        cout<<s<<" ";
    for(j=2;j<=10;j++)
 {
     cout<<ans[j]<<" ";

 }
 hua++;
 cout<<"\n";
 if(hua==50)
    break;
 }
 p=p+2;
 }
    return 0;
}
