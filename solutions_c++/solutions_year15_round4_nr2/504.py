#include<cstdio>
#include<algorithm>
#include<vector>
#include<cstring>
#include<set>
#include<assert.h>
using namespace std;
#define FOR(i,a,b) for(int i = a; i <= b; ++i)
#define FORD(i,a,b) for(int i = a; i >= b; --i)
#define REP(i,n) FOR(i,0,(n)-1)
#define RI(i,n) FOR(i,1,n)
#define pb push_back
#define mp make_pair
#define st first
#define nd second
#define mini(a,b) a=min(a,b)
#define maxi(a,b) a=max(a,b)
bool debug;
typedef vector<int> vi;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
const int inf = 1e9 + 5;
const int nax = 1000;

const long double EPS = 1e-10;

int n,testy;
ld v,x;
pair<ld,ld> t[nax];

bool check(ld s) {
	//minimalna
	ld akt_obj = 0., akt_temp = 0.;
	REP(i,n) {
		ld obj = s * t[i].nd;
		ld y = min(obj, v - akt_obj);
		akt_obj += y;
		akt_temp += y * t[i].st;
	}
	
	if (v - akt_obj > EPS || akt_temp - v*x > EPS)
		return false;

	//maksyma
	akt_obj = 0., akt_temp = 0.;
	FORD(i,n-1,0) {
		ld obj = s * t[i].nd;
		ld y = min(obj, v - akt_obj);
		akt_obj += y;
		akt_temp += y * t[i].st;
	}
	
	if (v - akt_obj > EPS || v*x - akt_temp > EPS)
		return false;
	return true;
}

int main(int argc, char * argv[]) {
	debug = argc > 1;
	scanf("%d",&testy);
	FOR(g,1,testy) {
		printf("Case #%d: ",g);
		scanf("%d",&n);
		scanf("%Lf%Lf",&v,&x);
		REP(i,n) scanf("%Lf%Lf",&t[i].nd,&t[i].st);
	
		sort(t,t+n);
		
		if (n == 1) {
			if (abs(t[0].st - x) > EPS)
				puts("IMPOSSIBLE");
			else
				printf("%.10Lf\n",v/t[0].nd);
		}
		else {
			if (t[1].st + EPS < x || t[0].st > x + EPS)
				puts("IMPOSSIBLE");
			else {
				if (abs(t[0].st - t[1].st) < EPS)
					printf("%.10Lf\n",v/(t[0].nd + t[1].nd));
				else {
					ld t1 = (v*x - v * t[1].st) / (t[0].nd * (t[0].st - t[1].st));
					ld t2 = (v - t1*t[0].nd) / t[1].nd;
					//printf("%Lf %Lf\n",t1,t2);
					printf("%.10Lf\n",max(t1,t2));
				}
				
			}
		}
	
	}
	return 0;
}
