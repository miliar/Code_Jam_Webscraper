#include <bits/stdc++.h>

#define FR(i,n) for(int i=0;i<n;i++)
#define FRI(iter, iterable) for(typeof((iterable).begin()) iter = (iterable).begin(); iter != (iterable).end(); ++iter)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define PI 3.1415926535897932384626433832795

typedef long long ll;
using namespace std;

void solve() {
	int N;
    string tmp;
    int ls[200];
    FR (i,200) ls[i]=0;
	cin >> tmp;
    FR (i,tmp.size()) ls[tmp[i]]++;
    vector <int> ns;
    while ( ls['Z'] > 0 ) {
    	ns.push_back(0);
		ls [ 'Z' ]--;
    	ls [ 'E' ]--;
    	ls [ 'R' ]--;
    	ls [ 'O' ]--;
	}
    while ( ls['W'] > 0 ) {
		ns.push_back(2);
		ls [ 'T' ]--;
    	ls [ 'W' ]--;
    	ls [ 'O' ]--;
	}
    while ( ls['X'] > 0) {
    	ns.push_back(6);
		ls [ 'S' ]--;
    	ls [ 'I' ]--;
    	ls [ 'X' ]--;
	}
    while ( ls['G'] > 0 ) {
    	ns.push_back(8);
		ls [ 'E' ]--;
    	ls [ 'I' ]--;
    	ls [ 'G' ]--;
    	ls [ 'H' ]--;
    	ls [ 'T' ]--;
	}
    while ( ls['S'] > 0 ) {
    	ns.push_back(7);
		ls [ 'S' ]--;
    	ls [ 'E' ]--;
    	ls [ 'V' ]--;
    	ls [ 'E' ]--;
    	ls [ 'N' ]--;
	}
    while ( ls['H'] > 0 ) {
    	ns.push_back(3);
		ls [ 'T' ]--;
    	ls [ 'H' ]--;
    	ls [ 'R' ]--;
    	ls [ 'E' ]--;
    	ls [ 'E' ]--;
	}
    while ( ls['R'] > 0 ) {
    	ns.push_back(4);
		ls [ 'F' ]--;
    	ls [ 'O' ]--;
    	ls [ 'U' ]--;
    	ls [ 'R' ]--;
	}
    while ( ls['O'] > 0) {
    	ns.push_back(1);
		ls [ 'O' ]--;
    	ls [ 'N' ]--;
    	ls [ 'E' ]--;
	}
    while ( ls['F']  > 0) {
    	ns.push_back(5);
		ls [ 'F' ]--;
    	ls [ 'I' ]--;
    	ls [ 'V' ]--;
    	ls [ 'E' ]--;
	}
    while ( ls['E'] > 0 ) {
    	ns.push_back(9);
		ls [ 'N' ]--;
    	ls [ 'I' ]--;
    	ls [ 'N' ]--;
    	ls [ 'E' ]--;
	}

	SORT (ns);
	FR (i,ns.size()) cout << ns[i];
	cout << endl;
	return;
}

int main(int argc, char **argv)
{
	cout << setiosflags(ios::fixed) << setprecision(10);  //double preceision
	FILE *istream, *ostream ;
	if (argc>1) {
		string infilename, outfilename;
		infilename=outfilename=argv[1];
		infilename+=".in";
		outfilename+=".out";
		if((istream = freopen(infilename.c_str(), "r", stdin)) == NULL) cout << "Wrong input file." ,exit(-1);
		if((ostream = freopen(outfilename.c_str(), "w", stdout)) == NULL) cout << "Wrong output file.", exit(-1);
	}
	else {
		if((istream = freopen("test.in", "r", stdin)) == NULL) cout << "Wrong input file." ,exit(-1);
	}
	int totaltestcases;
	cin >> totaltestcases;
	FR (testcase,totaltestcases) {
		cout << "Case #" << testcase + 1 << ": ";
		solve();
	}
}
