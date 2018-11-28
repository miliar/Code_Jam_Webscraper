#include<iostream>
#include<cstring>
#include<stdio.h>
#include<algorithm>
#include<cmath>
#include<vector>
#include<queue>
#include<deque>
#include<stack>
#include<map>
#include<set>
#define mp make_pair
#define pb push_back
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define F first
#define Se second
#define ll long long
#define pp pair<int,int>
#define INF 2000000000
using namespace std;
int T,t,i,j;
double C,F,X,ANS,timer,add;


main()
{freopen("B-small-attempt0.in","r",stdin);
 freopen("output.txt","w",stdout);
 scanf("%d",&T);
 for(t=1;t<=T;t++){
     cin>>C>>F>>X;
     ANS=X/2.;
     
     timer=0;
     add=2.0;
     for(i=1;i<=10000;i++){
         timer+=C/add;
         add+=F;
         if(timer+X/add<ANS)ANS=timer+X/add;
         }         
     cout<<"Case #"<<t<<": ";          
     printf("%.7lf\n",ANS);
    }
}
