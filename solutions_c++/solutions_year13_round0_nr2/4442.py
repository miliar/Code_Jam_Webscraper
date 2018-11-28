#include <stdio.h>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <string>
#include <vector>
#include <map>
using namespace std;

FILE *fin=freopen("input.txt","r",stdin);
FILE *fout=freopen("output.txt","w",stdout);

const int N=200;

int t,tt,n,m,i,j,a[N][N],b[N][N],rmx[N],cmx[N];
string answer;

main()
{
 cin>>tt;
 for ( t=1;t<=tt;t++ )
  {
   cin>>n>>m;

   for ( i=1;i<=n;i++ ) rmx[i]=0;
   for ( j=1;j<=m;j++ ) cmx[j]=0;

   for ( i=1;i<=n;i++ )
    for ( j=1;j<=m;j++ )
     {
      cin>>a[i][j];
      rmx[i]=max(rmx[i],a[i][j]);
      cmx[j]=max(cmx[j],a[i][j]);
     }

   for ( i=1;i<=n;i++ )
    for ( j=1;j<=m;j++ )
     b[i][j]=min(rmx[i],cmx[j]);

   answer="YES";
   for ( i=1;i<=n;i++ )
    for ( j=1;j<=m;j++ )
     if ( b[i][j]!=a[i][j] )
      answer="NO";

   cout<<"Case #"<<t<<": "<<answer<<endl;
  }
}
