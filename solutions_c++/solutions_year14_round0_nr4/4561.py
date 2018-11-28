/*

 E-Mail : ahmed.aly.tc@gmail.com
 TopCoder Handle : ahmed_aly

 Just For You :)

 */

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
int n;

//#define SMALL
#define LARGE
int main() {
//	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("D-small.in","rt",stdin);
	freopen("D-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("D-large.in","rt",stdin);
	freopen("D-large.out","wt",stdout);
#endif

	
	cin >> N;
	rep2(nn,1,N+1) {
		cin>>n;
		vd Naomi,Ken;
		rep(i,n){
			double c;
			cin>>c;
			Naomi.pb(c);
		}
		rep(i,n){
			double c;
			cin>>c;
			Ken.pb(c);
		}
		printf("Case #%d: ", nn);
		sort(all(Naomi));
		sort(all(Ken));
		
		vd Naomi1 = vd(Naomi);
		vd Ken1 = vd(Ken);
		int win1 = 0;
		rep(i,n){
			rep(j,n){
				if(Ken1[j]>0){
					if(Naomi1[i]<=Ken1[j]){
						for(int k=n-1;k>=0;k--)
							if(Ken1[k]>0){
								Ken1[k]=-1;
								goto END;
							}
					}else{
						Ken1[j]=-2;
						goto END;
					}
				}
			}
			END:;
		}
		rep(i,n)
			if(Ken1[i]!=-1)
				win1++;
		cout<<win1<<" ";
		
		vd Naomi2 = vd(Naomi);
		vd Ken2 = vd(Ken);
		int win2 = 0;
		rep(i,n){
			bool have = false;
			rep(j,n){
				if(Naomi2[i] < Ken2[j]){
					Ken2[j] = -1;
					have = true;
					break;
				}
			}
			if(!have)
				rep(j,n){
					if(Ken2[j]!=-1){
						Ken2[j]=-2;
						break;
					}
				}
		}
		rep(i,n)
			if(Ken2[i]!=-1)
				win2++;
		cout<<win2<<endl;
	}
	return 0;
}
