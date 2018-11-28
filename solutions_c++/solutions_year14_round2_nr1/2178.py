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
#define LOOPP(i,b,n)    for(int i=(b);i<(int)(n);++i)
#define PB	push_back
typedef vector<double>    VD;
typedef vector<string>    VS;
int gcd(int a, int b) { return (b == 0 ? a : gcd(b, a % b)); }

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
int t;sc(t);
LOOP(ts,t){

int n ;sc(n);
	if(n == 0){
		printf("Case #%d: %d\n",ts+1,0);
	   continue;
	}
	string a,b;
	cin>>a;cin>>b;
	int ca=0,cb=0,ia=0,ib=0;
	int gool = 0;
	bool g=true;
	while(ia < SZ(a) && ib < SZ(b)){
		if(a[ia] != b[ib]){
			g=false;
		    break;
		}
		ca=0;cb=0;
		while(ia < SZ(a) && a[ia] == a[ia+1]){
			ia++;ca++;
		}

		while(ib < SZ(b) && b[ib] == b[ib+1]){
			ib++;cb++;
		}
      ia++;ib++;
		gool += abs(cb-ca);
	}
	if(!(ia ==SZ(a) && ib ==SZ(b)))
		g=false;
	if(g)
		printf("Case #%d: %d\n",ts+1,gool);
	else
		printf("Case #%d: Fegla Won\n",ts+1);

}
			return 0;
}
