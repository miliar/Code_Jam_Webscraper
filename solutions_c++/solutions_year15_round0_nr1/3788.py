#include <iostream>
#include <string>
#include <vector>

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,b) FOR(i,0,b)

using namespace std;

char *in = "in.txt";
char *out = "out.txt";

int t;
vector< int > m,r;
vector< string > s;


int main(){
	freopen(in, "r", stdin);
	freopen(out, "w", stdout);
	cin >> t;
	m.resize(t);
	s.resize(t);
	r.resize(t);

	REP(i, t){
		cin >> m[i] >> s[i];
//		cout << m[i] << ' ' << s[i] << endl;
		int q = 0;
		REP(j, m[i] + 1){
			if (j > r[i] + q){
				r[i] += j - r[i] - q;
			}
			q += s[i][j] - '0';
		}
		cout << "Case #" << i+1 << ": " << r[i] << endl;
	}
	exit(0);
}
