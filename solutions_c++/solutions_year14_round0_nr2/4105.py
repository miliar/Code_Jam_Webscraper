/*
*
* solved by Ahmed Kamal
*/
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<iostream>
#include<sstream>
#include<cstring>
#include<vector>
#include<list>
#include<map>
#include<set>
#include<bitset>
#include<queue>
#include<utility>
#include<algorithm>
#include<functional>

using namespace std;

typedef long long int LL ;
#define vi vector<int> 
#define ii pair<int,int> 
#define vii vector< pair<int,int> > 
#define sc(x) scanf("%d",&x)
double const EPS = 2.22045e-016;
#define INF (1<<29)

#define ALL(v)				((v).begin()), ((v).end())
#define SZ(v)				((int)((v).size()))
#define CLR(v, d)			memset(v, d, sizeof(v))
#define LOOP(i, n)		for(int i=0;i<(int)(n);++i)

#define PB	push_back
typedef vector<double>    VD;
typedef vector<string>    VS;
int gcd(int a, int b) { return (b == 0 ? a : gcd(b, a % b)); }

int main()
{
   // freopen("input.txt","r",stdin);
   // freopen("output5.txt","w",stdout);
 double c,f,x;
int ts; sc(ts);
LOOP(tst,ts){
 cin>>c>>f>>x;
 double r = 2;
 double tt=0,co=0;
double tc,tnc,tx;
 while(true){
	 if(x - co -c < EPS ) //finish
	 {
	    tt+=((x-co)/r);
		break;
	 }
   tc = c/r;
   tnc = x/(r+f);
   tx = (x-co)/r;

   if(tx -(tc+ tnc) > EPS){ //buy farm
    co=0;
	tt+=tc;
	r=r+f;
   }
   else{ //finish with this rate
    tt+=tx;
	break;
   }
 
  }

 printf("Case #%d: %.7llf\n",tst+1,tt);
}

return 0; 
}
