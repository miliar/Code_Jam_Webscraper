#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define X real()
#define Y imag()
#define length(V) (hypot((V).X,(V).Y))
#define vect(a,b) ((b)-(a))
#define cross(a,b) ((conj(a)*(b)).imag())
#define normalize(v) ((v)/length(v))
#define rotate(p,about,theta) ((p-about)*exp(point(0,theta))+about)
#define pointEqu(a,b) (comp(a.X,b.X)==0 && comp(a.Y,b.Y)==0)

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0);
const double eps = 1e-9;


inline int comp(const double &a, const double &b) {
	if (fabs(a - b) < eps)
		return 0;
	return a > b ? 1 : -1;
}

#define SMALL
//#define LARGE

int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("A-small.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif

	int T;
	cin >> T;

	string temp;
	getline(cin, temp);

	for (int t = 0; t < T; t++) {
		int answer1;

		cin >> answer1;
		getline(cin, temp);

		vector<vector<int> > arrangement1;
		
		int number;
		for (int i = 0; i < 4; i++) {
			vector<int> rowBuilt;

			getline(cin, temp);
			stringstream ss(temp);
			for (int j = 0; j < 4; j++) {
				ss >> number;
				rowBuilt.push_back(number);
			}

			arrangement1.push_back(rowBuilt);
		}
		
		int answer2;

		cin >> answer2;
		getline(cin, temp);

		vector<vector<int> > arrangement2;
		
		for (int i = 0; i < 4; i++) {
			vector<int> rowBuilt;

			getline(cin, temp);
			stringstream ss(temp);
			for (int j = 0; j < 4; j++) {
				ss >> number;
				rowBuilt.push_back(number);
			}

			arrangement2.push_back(rowBuilt);
		}

		vector<int> options1 = arrangement1[answer1 - 1];
		vector<int> options2 = arrangement2[answer2 - 1];

		vector<int> solutions;
		int i = 0;
		while (i < options1.size()) {
			int j = 0;
			while (j < options2.size()) {
				if (options1[i] == options2[j]) {
					solutions.push_back(options1[i]);
					options1.erase(options1.begin() + i);
					options2.erase(options2.begin() + j);
					i--;
					j--;
				}
				j++;
			}
			i++;
		}

		cout << "Case #" << (t + 1) << ": ";
		if (solutions.size() < 1) {
			cout << "Volunteer cheated!";
		}
		else if (solutions.size() > 1) {
			cout << "Bad magician!";
		}
		else {
			cout << solutions[0];
		}
		cout << endl;
	}

	
	return 0;
}
