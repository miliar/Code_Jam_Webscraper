#include <iostream>
#include <fstream>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <utility>
using namespace std;

ifstream fin ("B.in");
ofstream fout ("B.out");
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> ii;
typedef long long ll;
typedef vector<ll> vll;
typedef vector<vll> vvll;
#define pb push_back
#define sz(a) int((a).size())
#define all(c) (c).begin(),(c).end()
#define abs(x) ((x)<0 ? -(x) : (x))

int main() {
	fout.setf( std::ios::fixed, std:: ios::floatfield );
	cout.setf( std::ios::fixed, std:: ios::floatfield );
	std::cout.precision(7);
	fout.precision(7);
	int T, c, n;
	fin >> T;
	double C, F, X, acum, acprev;
	for (c = 1; c <= T; c++) {
		fin >> C >> F >> X;
		acprev = X;
		acum = X/2.0;
		for (n = 1; acprev > acum; n++) {
			acprev = acum;
			acum -= X/(2.0 + (n-1)*F);
			acum += C/(2.0 + (n-1)*F);
			acum += X/(2.0 + n*F);
		}
		cout << n << endl;
		fout << "Case #" << c << ": " << acprev << endl;

	}
	return 0;
}
