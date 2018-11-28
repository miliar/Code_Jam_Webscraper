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
vector<int> v;

int main(){
	freopen(in, "r", stdin);
	freopen(out, "w", stdout);
	cin >> t;
	
	REP(k, t){
		int y = 0, z = 0, n, inc = 0;
		cin >> n;
		v.resize(n);
		REP(i, n)
			cin >> v[i];

		FOR(i, 1, n){
			if (v[i] >= v[i - 1])
				;
			else{
				y += v[i - 1] - v[i];
				inc = max(inc, v[i - 1] - v[i]);
			}
		}
		//int sp = inc / 10 + ((inc % 10) ? 1 : 0);

		REP(i, n - 1){
			if (v[i] > inc)
				z += inc;
			else
				z += v[i];
		}
		//z = sp;
		cout << "Case #" << k + 1 << ": " << y << " " << z << endl;
	}
	exit(0);
}
