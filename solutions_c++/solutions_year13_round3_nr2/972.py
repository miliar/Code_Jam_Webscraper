//--BY--©--WA-
#include<iostream> //cout, cin, getline

#include<algorithm> //find, reaplce, swap, sort, lower_bound, uper_bound, binnary_search...
#include<vector> //push_back, size, resize, 
#include<string>
#include<queue> //empty, front, back, push
#include<stack> //push, top, empty
#include<map>
#include<set>
#include<list> //spajazny zoznam .. vsetko v O(1)

#include<stdio.h> //printf, scanf, getchar, putchar
#include<math.h> //cos, sin, exp, pow, sqrt,  flnoor, cell
#include<stdlib.h> //atio, atl, strtod, strtol, atof, abs, 
#include<ctype.h> //isalnum, isalpha, isdigit, islower, isupper, toupper, tolower, 
#include<string.h> //strcm, strstr, strlen,

using namespace std;

#define FOREACH(obj,it) for(__typeof(obj.begin()) it = (obj).begin(); it != (obj).end(); (it)++)
#define FOR(i,a,b) for(int i=a; i<=b; i++)
#define FORD(i,a,b) for(int i=a; i>=b; i--)
#define REP(i,a,b) for(int i=a; i<b; i++)
#define DEBUG(V,S) FOR(i,0,S-1){cout << i << ". " << V[i] << endl;}

#define PB push_back
#define PII pair<int,int>
#define PLL pair<ll,ll>
#define MP make_pair
#define fi first
#define se second

#define SIZE(s) (int) (s).size()

#define INF 987654321
#define EPS 1e-9
#define ld long double // %Lf, double %lf
#define ll long long   // %llf

//--------------------------------------------------------------------------------------

map<PII, string> stav;
queue<pair< PII, int> > q;
int T;
int X, Y;

bool oob(int a) {
	if (a < -1000 || a > 1000) return true;
	return false;
}

void bfs() {
	while(!q.empty()) {
		pair< PII, int> a = q.front();
		q.pop();

		if (a.fi.fi == X && a.fi.se == Y) return ;

		string s = stav[MP(a.fi.fi, a.fi.se)];

		PII p;

		if (!oob(a.fi.fi+a.se)) {
			p = MP(a.fi.fi+a.se, a.fi.se);
			if (stav.find(p) == stav.end()) {
				stav[p] = s+"E";
				q.push(MP(p, a.se+1));
			}
		}

		if (!oob(a.fi.fi-a.se)) {
			p = MP(a.fi.fi-a.se, a.fi.se);
			if (stav.find(p) == stav.end()) {
				stav[p] = s+"W";
				q.push(MP(p, a.se+1));
			}
		}

		if (!oob(a.fi.se+a.se)) {
			p = MP(a.fi.fi, a.fi.se+a.se);
			if (stav.find(p) == stav.end()) {
				stav[p] = s+"N";
				q.push(MP(p, a.se+1));
			}
		}

		if (!oob(a.fi.se-a.se)) {
			p = MP(a.fi.fi, a.fi.se-a.se);
			if (stav.find(p) == stav.end()) {
				stav[p] = s+"S";
				q.push(MP(p, a.se+1));
			}
		}
	}
}

int main()
{	
	scanf("%d", &T);
	FOR (caser, 1, T) {
		scanf("%d %d", &X, &Y);

		stav.clear();
		stav[PII(0,0)] = "";
		while (!q.empty()) q.pop();
		q.push(MP(MP(0,0), 1));

		bfs();
		printf("Case #%d: ", caser);
		cout << stav[MP(X,Y)] << endl;
	}
	return 0;
}
