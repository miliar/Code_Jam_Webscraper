#include <cstdio>
#include <cmath>
#include <cctype>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <stack>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <map>
using namespace std;
typedef long long ll;
int main()
{
          freopen("B-large.in","r",stdin);
          freopen("GCJ132.out","w",stdout);
          long i,j,c,N,M,T,maxhang[101],maxcot[101],a[101][101];
          bool ok;
          cin>>T;
          for (c=1; c<=T; c++)
          {
                    cin>>N>>M;
                    ok=true;
                    for (i=1; i<=N; i++) maxhang[i]=0;
                    for (i=1; i<=M; i++) maxcot[i]=0;
                    for (i=1; i<=N; i++)
                    {
                              for (j=1; j<=M; j++)
                              {
                                        cin>>a[i][j];
                                        if (a[i][j]>maxhang[i]) maxhang[i]=a[i][j];
                                        if (a[i][j]>maxcot[j]) maxcot[j]=a[i][j];
                              }
                    }
                    for (i=1; i<=N; i++)
                    {
                              for (j=1; j<=M; j++)
                              {
                                        if ((a[i][j]<maxhang[i]) && (a[i][j]<maxcot[j])) 
                                        {
                                                                 ok=false;
                                        }
                              }
                    }
                    cout<<"Case #"<<c<<": ";
                    if (ok==true) cout<<"YES"<<endl;
                    if (ok==false) cout<<"NO"<<endl;
          }
          //system("pause");
          return 0;
}
