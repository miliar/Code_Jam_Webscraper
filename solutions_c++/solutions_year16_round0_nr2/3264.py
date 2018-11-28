#include <bits/stdc++.h>

#define FR(i,en) for(int i=0; i<(en); i++)
#define FRR(i,en) for(int i=(en-1); i>=0; i--)
#define FOR(i,st,en) for(int i=(st); i<(en); i++)
#define FORR(i,st,en) for(int i=(en-1); i>=(st); i--)
#define FRI(it, x) for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)

#define ALL(c) (c).begin(), (c).end()
#define SZ(i) i.size()
#define SORT(c) sort(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define PI 3.1415926535897932384626433832795

typedef long long ll;
using namespace std;

int main(int argc, char **argv)
{
	cout << setiosflags(ios::fixed) << setprecision(10);  //correct double
	FILE *istream, *ostream, *logstream  ;
	logstream = freopen("logdata.log","w",stderr);
	if (argc>1) {
		string infilename=argv[1], outfilename=argv[1];
		infilename+=".in";
		outfilename+=".out";
		if((istream = freopen(infilename.c_str(), "r", stdin)) == NULL) cout << "Wrong input file." ,exit(-1);
		if((ostream = freopen(outfilename.c_str(), "w", stdout)) == NULL) cout << "Wrong output file.", exit(-1);
	}
	int totaltestcases, c, p;
	char last;
	string s;
	cin >> totaltestcases;
	FR (testcase,totaltestcases) {
		cout << "Case #" << testcase + 1 << ": ";
		cin >> s;
		c = 0;
		p = 0;
		last = '0';
		FR (i,s.length()) {
			if ( last != s[i] ) {
				if ( s[i] == '+') p = 1;
				if ( s[i] == '-' ) c = c + p + 1;
				last = s[i];
			}
		}
		cout << c << "\n";
	}
}
