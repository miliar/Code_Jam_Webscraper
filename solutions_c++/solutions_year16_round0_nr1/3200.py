#include <bits/stdc++.h>
#include <sstream>

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
	ll totaltestcases, N, c;
	cin >> totaltestcases;
	FR (testcase,totaltestcases) {
		cin >> N;
		cout << "Case #" << testcase + 1 << ": ";
		if ( N != 0 ) {
			set<int> numbers;
			FR (i,10) {
				numbers.insert(i);
			}
			c=0;
			do {
				c+=N;
				std::string tmp;
				std::stringstream tmps;
				tmps << c;
				tmps >> tmp;
				FR(i,tmp.length()) {
					numbers.erase(tmp[i] - 48);
				}
			} while ( !numbers.empty());
			cout << c << "\n";
		}
		else {
		  cout << "INSOMNIA\n";
		}
	}
}
