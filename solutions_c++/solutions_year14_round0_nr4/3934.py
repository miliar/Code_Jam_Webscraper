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
   // freopen("D-large.in","r",stdin);
   // freopen("dddD.txt","w",stdout);
	int tst;sc(tst);
	vector<double> N,D;
	vector<double>::iterator it;

LOOP(ts,tst){
	int f=0,s=0;
	int n;sc(n);
	N.assign(n,0.0);D.assign(n,0.0);
	LOOP(i,n)
		 cin>>N[i];
	LOOP(i,n)
		 cin>>D[i];
	sort(ALL(N));  sort(ALL(D));
	VD NN = N;
	VD DD = D;
	// calc for war
	LOOP(i,n){
		double val = N[i];
		it = upper_bound(ALL(D),val);
		if(it == D.end()){
		  f +=n-i;
		  break;
		}
		else{
			D.erase(it);
		}
	}

	//calc for deceitful war
	LOOP(i,n){
	 if(NN[SZ(NN)-1] > DD[SZ(NN)-1]){
	  s++;
	  NN.erase(NN.end()-1);
	  DD.erase(DD.end()-1);
	 }
	 else{
		 NN.erase(NN.begin());
		 DD.erase(DD.end()-1);
	 }
	}
	printf("Case #%d: %d %d\n",ts+1,s,f);
}

return 0; 
}
