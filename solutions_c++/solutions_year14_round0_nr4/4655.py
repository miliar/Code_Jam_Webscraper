#include<iostream>
#include<stdio.h>
#include<string.h>
#include<math.h>
#include<vector>
#include<queue>
#include<map>
#include<stdlib.h>
#include<algorithm>
#define i_n(a) scanf("%d",&a)
#define l_n(a) scanf("%I64d",&a)
#define LL long long int
#define pb(a) push_back(a)
#define i_p(a) printf("%d\n",a)
#define l_p(a) printf("%I64d\n",a)
#include<limits.h>

using namespace std;
int maximum(int a,int b)
{
    if(a>b)
        return a;
    else
    return b;
}
bool cmp(const pair<int, int>& firs, const pair<int, int>& sec)
 {
  return firs.first < sec.first;
 }
 int fn(string s)
 {
     int l,i,t=1;
     int ans=0,val=100000;
     l=s.size();
     int tm=l-2;
     for(i=2;i<l;i++)
     {
      ans*=10;
      ans+=s[i]-'0';
     }
    // i_p(ans);
     for(i=0;i<tm;i++)
        t=t*10;
     val/=t;
     ans*=val;
   return ans;
}
int mark[1000005]={0};
int main()
{
int t,k,n,i,z;
i_n(t);
for(k=1;k<=t;k++)
{
    i_n(n);
    memset(mark,0,sizeof(mark));
    int  in[1005],out[1005];
    //double val=100000.00;
    string tm="";
    for(i=0;i<n;i++)
    {
        cin>>tm;
        z=fn(tm);
        in[i]=z;
    }
    for(i=0;i<n;i++)
    {
        cin>>tm;
        z=fn(tm);
        out[i]=z;
        //mark[z]=1;
    }
    sort(in,in+n);
    sort(out,out+n);
   int cn;
    cn=0;
    /*for(i=0;i<n;i++)
    {
        cout<<in[i]<<" ";

    }
    cout<<endl;
    for(i=0;i<n;i++)
    {
      cout<<out[i]<<" ";

    }
    cout<<endl;*/
    int prev=-1,j;
    for(i=0;i<n;i++)
    {
        for(j=prev+1;j<n;j++)
        {
            if(in[i]>out[j])
            {
                cn++;
                prev=j;
                break;
            }

        }
    }
    printf("Case #%d: %d ",k,cn);
    cn=0;
    for(i=0;i<n;i++)
    {
        int tm=0;
        for(j=0;j<n;j++)
        {
            if(in[i]>out[j])
                tm++;
            else
            {
              if(mark[out[j]]==1)
                        tm++;
              else
              {
                mark[out[j]]=1;
                break;
              }
            }
        }
        if(tm==n)
            cn++;
    }
    printf("%d\n",cn);
}
 return 0;
}
