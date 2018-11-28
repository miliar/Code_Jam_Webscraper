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

double projectGoalReachedTime(double target, double production, double currentCookies) {
	double requiredCount = target - currentCookies;
	double requiredTime = requiredCount / production;
	return requiredTime;
}

//#define DEBUG
//#define SMALL
#define LARGE

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

	int N;
	cin >> N;

	string temp;
	getline(cin, temp);

	cout << setprecision(7) << fixed;

	for (int n = 0; n < N; n++) {
		getline(cin, temp);
		istringstream iss(temp);

		double C;
		double F;
		double X;

		iss >> C;
		iss >> F;
		iss >> X;

		double currentCookies = 0;
		double currentTime = 0;
		double currentProduction = 2;

		double factoryBuyChoiceTime;
		double victoryTime;

		double withFactoryVictoryTime;
		double withoutFactoryVictoryTime;

		while (currentCookies < X) {
#ifdef DEBUG			
			cout << currentTime << ": " << currentCookies << " out of " << X << " with production of " << currentProduction << endl;
#endif
			if (currentCookies < C) {
				factoryBuyChoiceTime = currentTime + (C - currentCookies) / currentProduction;
				victoryTime = currentTime + (X - currentCookies) / currentProduction;
			
				if (victoryTime < factoryBuyChoiceTime) {
#ifdef DEBUG			
					cout << "No need to buy!" << endl;
#endif
					// We win without doing anything else
					currentTime = victoryTime;
					currentCookies = X;
				}
				else {
#ifdef DEBUG			
					cout << "Check at next decision point!" << endl;
#endif
					// Jump to the next decision point
					currentTime = factoryBuyChoiceTime;
					currentCookies = C;
				}
			}

			if (currentCookies < X) {
				// Now decide whether we will need another factory
				withoutFactoryVictoryTime = currentTime + (X - currentCookies) / currentProduction;
				withFactoryVictoryTime = currentTime + (X - (currentCookies - C)) / (currentProduction + F);

#ifdef DEBUG			
				cout << "With, we win at " << withFactoryVictoryTime << " and without, we win at " << withoutFactoryVictoryTime << endl;
#endif
			
				if (withoutFactoryVictoryTime <= withFactoryVictoryTime) {
#ifdef DEBUG			
					cout << "We win!" << endl;
#endif
					// Jump to end!
					currentTime = withoutFactoryVictoryTime;
					currentCookies = X;
				}
				else {
#ifdef DEBUG			
					cout << "Let's buy that factory!" << endl;
#endif
					// Buy factory
					currentCookies -= C;
					currentProduction += F;
				}
			}

		}

		cout << "Case #" << (n + 1) << ": " << currentTime << endl;
	}

	
	return 0;
}
