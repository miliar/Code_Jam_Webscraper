//TAG : 

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cstring>
#include<cmath>
#include<vector>
#include<stack>
#include<map>
#include<queue>
#include<algorithm>
#include <climits>
using namespace std;

#define rep(i,n)	for(int (i)=0;(i)<(n);(i)++)
#define repd(i,n)	for(int (i)=(n)-1;(i)>=0;(i)--)
#define REP(i,n) for (int (i)=0,_n=(n); (i) < _n; (i)++)
#define FOR(i,a,b) for (int _b=(b), (i)=(a); (i) <= _b; (i)++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))

#define CLEAR(x) memset((x),0,sizeof(x));
#define CLEARA(x) memset(&(x),0,sizeof(x));
#define FILL(x,v) memset((x),(v),sizeof(x));
#define FILLA(x,v) memset(&(x),(v),sizeof(x));

#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 0x7fffffff
#define X first
#define Y second
#define pb push_back
#define SZ(c) (int)(c).size()
#define MP make_pair
//const double pi = acos(-1.0);
#define EPS 1e-9

int n;
double naomi[1000],ken[1000];

int solve_optimal()
{
	int a=0,b=0;//a,naomi,b,ken
	int value=0;
	vector<double> ken_ken(ken,ken+n);
	for(;a<n;a++){
		if(naomi[a]>ken_ken[a]){
			vector<double> shifted;
			do{
				shifted.pb(ken_ken[a]);
				ken_ken.erase(ken_ken.begin()+a);
			}while(ken_ken.size()>a && naomi[a]>ken_ken[a]);
			if(a<ken_ken.size())
				ken_ken.insert(ken_ken.end(),ALL(shifted));
			else{
				//All naomi win vs ken's
				return n-a;
			}
		}
	}
	return 0;
}

int solve_deceit()
{
	int a=0,b=0;//a,naomi,b,ken
	int value=0;
	for(;a<n;a++){
		if(naomi[a]>ken[b]){
			b++;
			value++;
		}	
	}
	return value;
}

int main()
{
	int test_case;
	scanf("%d",&test_case);
	FOR(t,1,test_case){
		scanf("%d",&n);
		rep(i,n)scanf("%lf",&naomi[i]);
		rep(i,n)scanf("%lf",&ken[i]);
		sort(naomi,naomi+n);
		sort(ken,ken+n);

		int deceit = solve_deceit();
		int opt = solve_optimal();
		
		printf("Case #%d: %d %d\n",t,deceit,opt);
		//Debug
		/*rep(i,n)printf("%lf ",naomi[i]);
		puts("");
		rep(i,n)printf("%lf ",ken[i]);
		puts("\n");*/
	}
	return 0;
}