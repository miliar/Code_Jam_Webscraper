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
int d[10000005];
long long i,x,y;
int T,t;

bool check(long long x){
     if(x%10==0)return 0;
     long long y=x,z=0;
     while(y)z=z*10+y%10,y/=10;
     if(x!=z)return 0;

     y=x*x;
     z=0;
     while(y)z=z*10+y%10,y/=10;
     if(x*x!=z)return 0;
     return 1;
}

main()
{freopen("C-large-1.in","r",stdin);
 freopen("output.txt","w",stdout);
 for(i=1;i<=10000000;i++){
    d[i]=d[i-1];
    if(check(i))d[i]++;
    }
 scanf("%d",&T);
 for(t=1;t<=T;t++){
     scanf("%lld%lld",&x,&y);
     cout<<"Case #"<<t<<": "<<d[(int)sqrt(y)]-d[(int)sqrt(x-1)]<<endl;
 }
}
