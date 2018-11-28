#include<iostream>
#include<cmath>
#include<string.h>
#include<stdio.h>
#include<algorithm>
using namespace std;


int t;
int n,r,p,s;



string gao(char w,int ff)
{
    int i,j,k;
    
    if(ff==n+1)
    {
        string tmp="";
        tmp.push_back(w);
        return tmp;
    }
    
    string ll=gao(w,ff+1);
    char nw=w+1;
    if(nw==4+'0')nw=1+'0';
    string rr=gao(nw,ff+1);
    
    
    //cout<<w<<' '<<ff<<"     "<<ll<<' '<<rr<<endl;
    
    if(ll<rr)
    {
        return ll+rr;
    }
    else
    {
        return rr+ll;
    }
    
}


string ans;
string ans0;
int main()
{
    int i,j,k,times;
    int cc[4];
    freopen("A-large.in","r",stdin);
    freopen("ans.out","w",stdout);
    
    
    scanf("%d",&t);
    
    for(times=1;times<=t;times++)
    {
         cin>>n>>r>>p>>s;
         ans="";
         ans.push_back('4');
         for(j=1;j<=3;j++)
         {
             ans0=gao(j+'0',1);
             
             memset(cc,0,sizeof(cc));
             for(i=0;i<(1<<n);i++)
             {
                 cc[ans0[i]-'0']++;
             }
             
             if(cc[1]==p && cc[2]==r && cc[3]==s)
             {
                 if(ans0<ans)
                 {
                     ans=ans0;
                 }
             }
             
         }
         
         cout<<"Case #"<<times<<": ";
         if(ans[0]=='4')
         {
             cout<<"IMPOSSIBLE"<<endl;
         }
         else
         {
             for(i=0;i<(1<<n);i++)
             {
                 if(ans[i]=='1')
                 {
                     cout<<'P';
                 }
                 else if(ans[i]=='2')
                 {
                     cout<<'R';
                 }
                 else
                 {
                     cout<<'S';
                 }
             }
             cout<<endl;
         }
    }
    
    
    return 0;
}
