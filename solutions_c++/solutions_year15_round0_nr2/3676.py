#include <iostream>
#include <string>
#include <vector>

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,b) FOR(i,0,b)
#define min(a,b) ((a)<(b))?(a):(b)
#define max(a,b) ((a)>(b))?(a):(b)

using namespace std;

char *in = "in.in";
char *out = "out.out";

int t;

const int MAX = 1001;
vector< int > p(MAX);

/*
int fun(int a){
	if (!f[a])
		//f[a] = min(fun(a / 2 + a % 2) + 1, a);
		f[a] = fun(a / 2 + a % 2) + 1;
	return	f[a];
}
*/

int m(int p, int e){
	int r = p / e;
	if (p%e)
		r++;
	r--;
	return r;
}

int main(){
	freopen(in, "r", stdin);
	freopen(out, "w", stdout);
	cin >> t;	
//	f[1] = 1;
	REP(i, t){
		int q = MAX*MAX, pmax = 0, d;
		cin >> d;
		REP(j, d){
			cin >> p[j];
			if (p[j] > pmax)
				pmax = p[j];
		}

		FOR(e, 1, pmax + 1){
			int temp = 0;
			REP(j, d)
				//				temp = max(temp, m(p[j], e) + e);
				temp += m(p[j], e);
			temp += e;
			q = min(q, temp);
		}
		cout << "Case #" << i + 1 << ": " << q << endl;
	}
	exit(0);
}
