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



#define SMALL
//#define LARGE
int main() {
	freopen("A-small-attempt0.in", "rt", stdin);
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("a_sample.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif

    int arrf[4][4];
	int arrs[4][4];
	int af=-1;
	int as=-1;
	int i=0,j=0,k=0;
	int cnt=0,num=0;
	cin >> N;
	//string s1;
	
	
	for (i=0;i<N;i++)
	{
        cnt=0;
        cin >> af;
        for (j=0;j<4;j++)
        scanf("%d %d %d %d",&arrf[j][0],&arrf[j][1],&arrf[j][2],&arrf[j][3]);
        cin >> as;
        for (j=0;j<4;j++)
        scanf("%d %d %d %d",&arrs[j][0],&arrs[j][1],&arrs[j][2],&arrs[j][3]);
     
        for ( j=0;j<4 && cnt<2;j++)
         for (k=0;k<4 && cnt<2;k++){
             //printf("%d\n",cnt);
         if(arrf[af-1][j] == arrs[as-1][k])
         {
                        num=arrf[af-1][j];
                        cnt=cnt+1;
                        
         }
         } 
         
        //printf("final count value %d\n",cnt);
         if (cnt > 1)            printf("Case #%d: Bad magician!\n",i+1);
         else if (cnt == 0)       printf("Case #%d: Volunteer cheated!\n",i+1);
         else if (cnt == 1)       printf("Case #%d: %d\n",i+1,num);
    /*     
	for (j=0;j<4;j++)
	printf("%d %d %d %d \n",arrf[j][0],arrf[j][1],arrf[j][2],arrf[j][3]);
	for (j=0;j<4;j++)
	printf("%d %d %d %d \n",arrs[j][0],arrs[j][1],arrs[j][2],arrs[j][3]); */
    }
	//getline(cin,s1);
	/*
	rep2(nn,1,N+1) {
		vs v;
		string s;
		getline(cin,s1);
		ss S(s1);
		while(S>>s)
			v.pb(s);
		reverse(all(v));
		printf("Case #%d:", nn);
		rep(i,v.sz)
			cout<<" "<<v[i];
		cout<<endl;
	}*/
	return 0;
}
