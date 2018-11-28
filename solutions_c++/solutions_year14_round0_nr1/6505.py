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
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define dot(a,b) ((conj(a)*(b)).X)
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

int di[] = { 1, -1, 0, 0, 1, -1, 1, -1 };
int dj[] = { 0, 0, 1, -1, 1, -1, -1, 1 };
int diK[] = { -2, -2, -1, 1, 2, 2, 1, -1 };
int djK[] = { -1, 1, 2, 2, 1, -1, -2, -2 };

int I, J;

inline bool val(const int &i, const int &j) {
	if (i < 0 || j < 0 || i >= I || j >= J)
		return false;
	return true;
}

int N, nn;
int main(int argc, char *args[]) {
	if (argc == 2 && strcmp(args[1], "small") == 0) {
		freopen("small.in","rt",stdin);
		freopen("small.out","wt",stdout);
	}
	else if (argc == 2 && strcmp(args[1], "large") == 0) {
		freopen("large.in","rt",stdin);
		freopen("large.out","wt",stdout);
	}
	else {
		freopen("a.txt", "rt", stdin);
	}

	cin>>N;

	int row1[4], row2[4], i, row, dummy;
	rep2(nn,1,N+1) {
		printf("Case #%d: ", nn);
		cin >> row;
		for (i = 1; i <= 4; i++) {
			if (i == row) {
				cin >> row1[0] >> row1[1] >> row1[2] >> row1[3];
			} else {
				cin >> dummy >> dummy >> dummy >> dummy;
			}
		}
		cin >> row;
		for (i = 1; i <= 4; i++) {
			if (i == row) {
				cin >> row2[0] >> row2[1] >> row2[2] >> row2[3];
			} else {
				cin >> dummy >> dummy >> dummy >> dummy;
			}
		}
		sort(row1, row1+4);
		sort(row2, row2+4);
		vector<int> intersection(8);
		vector<int>::iterator it = set_intersection(row1,row1+4,row2,row2+4, intersection.begin());
		intersection.resize(it-intersection.begin());
		if (intersection.size() == 1) {
			cout << intersection[0];
		} else if (intersection.size() == 0) {
			cout << "Volunteer cheated!";
		} else {
			cout << "Bad magician!";
		}
			
		cout<<endl;
	}

	return 0;
}
