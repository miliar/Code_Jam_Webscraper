#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<cmath>
#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
#define pb push_back
#define mp make_pair
#define F first
#define S second
using namespace std;
int n,m,i,j,a[105][105],t,T;
int p[105],q[105];

bool check(){
     int i,j;
     for(i=1;i<=n;i++)
        for(j=1;j<=m;j++)
        if(a[i][j]<p[i] && a[i][j]<q[j])return 0;
     return 1;
}

main()
{freopen("B-large.in","r",stdin);
 freopen("output.txt","w",stdout);
 scanf("%d",&T);
 for(t=1;t<=T;t++){
    scanf("%d%d",&n,&m);
    for(i=1;i<=n;i++)
        for(j=1;j<=m;j++)
        scanf("%d",&a[i][j]);
    for(i=1;i<=n;i++)p[i]=0;
    for(j=1;j<=m;j++)q[j]=0;

    for(i=1;i<=n;i++)
      for(j=1;j<=m;j++){
            p[i]=MAX(p[i],a[i][j]);
            q[j]=MAX(q[j],a[i][j]);
    }

    if(check())cout<<"Case #"<<t<<": YES"<<endl;else
        cout<<"Case #"<<t<<": NO"<<endl;
 }
}
