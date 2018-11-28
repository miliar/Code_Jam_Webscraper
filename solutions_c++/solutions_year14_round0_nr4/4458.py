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

//#define SMALL
#define LARGE
int main() {
#ifdef SMALL
	freopen("D-small.in","rt",stdin);
	freopen("D-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("D-large.in","rt",stdin);
	freopen("D-large.out","wt",stdout);
#endif


	const int MAXN = 10000;
	int N, M, K, i, j, k, l, nn;
	double fun[MAXN];
	double fun2[MAXN];
	int bad = 0;
	string s; 
	char a[MAXN];
	char input[MAXN];

	scanf("%d", &T);
	rep2(nn,1,T+1) {  //Number of test cases
// 		scanf("%d %d", &N, &M);  //Read two integers
		int tmp=0;
/*		rep(i,N)rep(j,M){
			scanf("%d", &tmp);
			board[i][j] = tmp;
		}   Read a matrix of integers */

/*		rep(i,N){
			scanf("%d", x+i);
		}  Read an integer array into one variable */

//		getline(cin, s); //Get string; s.sz()
//		scanf("%s", &a[1]) //Get string into array of characters starting from 1
//		scanf("%s", &dat[i][1]) //Get list of strings into 2-d array of characters
//		scanf("%s", input) //Get string into variable starting from 0; strlen(input)
//		set <string> S; rep(i,n){string s; cin >>s; S.insert(s);} //Set of strings to use later to compare. 
//		scanf("%d%d", &b[i],&c[i]); //Int array of paired numbers
//		rep(i,N){cin>>arr[i];} //Get's array of integers from input line of numbers with known length


//		while (iss >> s) {ss.pb(s)} //Puts s values into separate containers in ss. (Seperated by spaces in s)


		scanf("%d", &N);  //Read number of blocks
		rep(i, N){
			scanf("%lf", &fun[i]);	 //Naomi
		}
		rep(i,N){
			scanf("%lf", &fun2[i]); // Ken
		}
		sort(fun, fun + N);
		sort(fun2, fun2 + N);

		float tmp1 =0.0;
		float tmp2 =0.0;
		
		int Naomi = 0;
		int Ken = 0;
		int point = 0;
		rep(i,N){
			tmp1 = fun[Naomi];
			tmp2 = fun2[Ken];
			if(tmp2 > tmp1){
				Naomi +=1;
			}
			else{
				Naomi +=1;
				Ken +=1;
				point +=1;
			}
		}

		Naomi = N-1;
		Ken = N-1;
		int point2 = 0;
		rep(i,N){
			tmp1 = fun[Naomi];
			tmp2 = fun2[Ken];
			if(tmp2 < tmp1){
				Naomi -=1;
				point2 +=1;
			}
			else{
				Naomi -=1;
				Ken -=1;
			}
		}

		gout<<point<<" "<<point2<<endl;

	}  //End number of test cases loop
	return 0;
}  // End main function