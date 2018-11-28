//Author: prakash.mishra005
#include<cstdio>
#include<vector>
#include<cmath>
#include<string>
#include<cstring>
#include<algorithm>
#include<queue>
#include<set>
#include<stack>
#include<map>
#include<sstream>
#include<bitset>
#include<deque>
#include<utility>
#include<cstdlib>
#include<iomanip>
#include<cctype>
#include<climits>
#include<iostream>
using namespace std;
#define ll             long long
#define ull            unsigned long long
string tostr(long long x) { stringstream ss; ss << x; return ss.str(); }
long long toint(const string &s) { stringstream ss; ss << s; long long x; ss >> x; return x; }

int n,m,a[101][101];
int row(int i)
{
    int t=a[i][0];
    for(int j=0;j<m;j++)
    if(a[i][j]!=t) return 0;
    return 1;
    }
int column(int j)
{
    int t=a[0][j];
    for(int i=0;i<n;i++)
    if(a[i][j]!=t) return 0;
    return 1;
    }
int main()
{
freopen("B-small-attempt0.in","r",stdin);
freopen("output.txt","w",stdout);
    int test,jkl=1;
    cin>>test;
    for(int k=1;k<=test;k++)
    {
                  int trace=1;
                  cin>>n>>m;
                  for(int i=0;i<n;i++)
                  for(int j=0;j<m;j++)
                  cin>>a[i][j];
                  int max=a[0][0];
                  for(int i=0;i<n;i++)
                  for(int j=0;j<m;j++)
                  if(a[i][j]>max) max=a[i][j];
                  int to[101][101];
                  for(int i=0;i<n;i++)
                  for(int j=0;j<m;j++)
                  to[i][j]=max;
                  for(int i=0;i<n;i++)
                  if(row(i)==1) {
                                int tem=a[i][0];
                                for(int j=0;j<m;j++)
                                to[i][j]=tem;
                                }
                  for(int j=0;j<m;j++)
                  {
                          if(column(j)==1) {
                                           int tem=a[0][j];
                                           for(int i=0;i<n;i++)
                                           to[i][j]=tem;
                                           }
                  }

                  for(int i=0;i<n;i++)
                  for(int j=0;j<m;j++)
                  if(a[i][j]!=to[i][j]) {trace=0;break;}

                  if(trace==1) cout<<"Case #"<<k<<": YES"<<endl;
                  else cout<<"Case #"<<k<<": NO"<<endl;

    }
return 0;
}
