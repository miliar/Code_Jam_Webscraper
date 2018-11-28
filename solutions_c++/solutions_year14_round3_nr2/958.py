#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <cassert>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include<stdio.h>

#define uniq(c) (c).resize(unique(c.begin(),c.end())-(c).begin());
#define all(a) a.begin(),a.end()
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define pb push_back
#define PI 3.14159265
#define eps 1e-10
#define ll long long
#define ULL unsigned long long
#define MOD 1000000007



using namespace std;
int SI(string str) {int ans; stringstream s; s<<str; s>>ans; return ans;}
string IS(int n) {string str; stringstream s; s<<n; s>>str; return str;}


//using namespace std;
ll gcd(ll a,ll b)
{
if(a%b==0)
return b;
else
return gcd(b,a%b);
}
int main()
{
    freopen("read.txt","r",stdin);
    freopen("write.txt","w",stdout);
    char str[101][101];
    int fre1[101][27];
    int t,k,i,f,j,len,ans;
    char ch;
    int p,q,tmp,tmp1;
    cin>>t;
    FOR(k,1,t+1)
    {
        ans=0;
        int n;
        int a[11];
         int f1=1;
 
         cin>>n;
        FOR(i,1,n+1)
         {
            for(j=1;j<=26;++j)
             {
               fre1[i][j]=0;
              }
          }

         FOR(i,1,n+1)
          a[i]=i;
          FOR(i,1,n+1)
         {
            cin>>str[i];
         }
         FOR(i,1,n+1)
         {
            for(j=0;j<strlen(str[i]);++j)
             {
                tmp=(int)str[i][j]-96;
                if(fre1[i][tmp]==0)
                fre1[i][tmp]++;
                 else
                 {
                    if(str[i][j]!=str[i][j-1])
                      {
                        f1=0;
                        break;
                      }
                  }
               }
         }
         int fre[27];
         cout<<"Case #"<<k<<": ";
         if(f1==1)
         {
           do
             {
               memset(fre,0,sizeof(fre));
               int f=1;
               for(j=1;j<=26;++j)
                 {
                    fre[j]=fre1[a[1]][j];
                 }
               FOR(i,2,n+1)
                  {
                    int ct=0;
                     for(j=1;j<=26;++j)
                      {
                        if(fre1[a[i]][j]==1 && fre[j]==1)
                          {
                             ct++;
                           }
                   }
                        if(ct>=2)
                         {
                            f=0;
                            break;
                          }
                        else if(ct==1)
                         {
                           if(str[a[i]][0]!=str[a[i-1]][strlen(str[a[i-1]])-1])
                            {
                                 f=0;
                                 break;
                            }
                }
          for(j=1;j<=26;++j)
          {
            if(fre1[a[i]][j]==1)
                {
                   fre[j]=1;
                 }
           }
 
          }
          if(f)
          {
            ans++;
          }
         }while(next_permutation(a+1,a+n+1));
       }
          cout<<ans<<endl; 
    }
return 0;
}
