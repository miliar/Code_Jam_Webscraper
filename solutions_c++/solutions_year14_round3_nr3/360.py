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
#define rep(i,m) for((i)=0;(i)<(int)(m);(i)++)
#define rep2(i,n,m) for((i)=n;(i)<(int)(m);(i)++)
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
typedef istringstream iss;
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
//const double PI = 2 * acos(0);
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

int dx[] = { 0, 0, 1, -1};
int dy[] = { 1, -1, 0, 0};

int I, J;

inline bool val(const int &i, const int &j) {
	if (i < 0 || j < 0 || i >= I || j >= J)
		return false;
	return true;
}

int T;
int n;
int case_number;

#define gout case_number++, printf("Case #%d: ",case_number), cout       

#define SMALL
//#define LARGE
int main() {
#ifdef SMALL
	freopen("C-small-attempt1.in","rt",stdin);
	freopen("C-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("C-large-practice.in","rt",stdin);
	freopen("C-large-practice.out","wt",stdout);
#endif

	const int MAXN = 55;
	int N, M, K, i, j, k, l, nn, inside, answer, loop, big;
	double fun[MAXN];
	double fun2[MAXN];
	int bad = 0;
	string s; 
	char a[MAXN];
	char input[MAXN];
	char d[MAXN][MAXN];

	scanf("%d", &T);
	rep2(nn,1,T+1) {  //Number of test cases
 		scanf("%d %d %d", &N, &M, &K);  //Read three integers
		int tmp=0;
		answer =0;
		bad=0;
		big=0;

		inside = (N-2)*(M-2);
		if(inside < 0)
		{
			answer = K;
			bad=1;
		}
		if((bad==0)&&((N==1)&&(M==1)))
		{
			answer=K;
			bad=1;
		}

		if((bad==0)&&((N==2)||(M==2)))
		{
			answer=K;
			bad=1;
		}

		if((bad==0)&&(K>=((N*M)-4)))
		{
			tmp=inside+2*(N + M - 4);
			answer=K-inside;
			bad=1;
		}

		if((bad==0)&&(K<=4))
		{
			answer=K;
			bad=1;
		}

		if((bad==0)&&(K==(N*M)-5))
		{
			answer=(N*M-4) - inside;
			bad=1;
		}

		if(bad==0)
		{
			loop = (N*M -4) - inside;
				if(N>=M)
				{
					j=N-2;
					k=M-2;
				}
				else
				{
					j=M-2;
					k=N-2;
				}
			answer = loop+inside;
			do 
			{
				N=j+1;
				M=k+2;
				inside = (j-1)*(k);
				loop= (N*M-4) - inside;
				answer = inside+loop;
				if(N>=M)
				{
					j=N-2;
					k=M-2;
				}
				else
				{
					j=M-2;
					k=N-2;
				}
			}while(K<answer-1);
			answer=loop;
			if(K>inside+loop)
			{
				answer = loop+1;			
			}
		}
		
			
			tmp=0;

		



		gout<<answer<<endl;

	}  //End number of test cases loop
	return 0;
}  // End main function