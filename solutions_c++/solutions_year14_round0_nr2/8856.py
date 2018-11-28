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

int N;
int arr[2009];
//#define SMALL
#define LARGE
int main() {
    freopen("a.txt", "rt", stdin);
#ifdef SMALL
    freopen("B-small-attempt1.in","rt",stdin);
    freopen("B-small.out","wt",stdout);
#endif
#ifdef LARGE
    freopen("B-large.in","rt",stdin);
    freopen("B-large.out","wt",stdout);
#endif
    scanf("%d", &N);
    rep2(nn,1,N+1) {
        double C = 0.0L;
        double F = 0.0L;
        double targetCookie = 0.0L;
        double cookieRate  = 2.0L;
        double totalCookie = 0.0L;
        double totalTime   = 0.0L;
        double FinalTime   = 0.0L;
        double targetTime  = 0.0L;
        double bestTime    = 0.0L;
        double diff        = 0.0L;
        cin >> setprecision(7) >> C;
        cin >> setprecision(7) >> F;
        cin >> setprecision(7) >> targetCookie;

        cout.setf( std::ios::fixed, std:: ios::floatfield ); // floatfield set to fixed
        cout.precision(7);
        
        diff = targetCookie - C;
        bestTime = targetCookie/cookieRate;
        
        while(totalCookie < targetCookie) {
            double farmTime = C/cookieRate;
            cookieRate = cookieRate + F;
            totalTime = totalTime + farmTime;
            totalCookie = totalCookie + C;
            diff = targetCookie - totalCookie;
            targetTime = targetCookie/cookieRate;
            FinalTime = totalTime + targetTime;
            if(FinalTime < bestTime) bestTime = FinalTime;
        }
        cout << "Case #" << nn << ": " << bestTime << endl;
    }
    return 0;
}
