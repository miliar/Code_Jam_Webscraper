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
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small-attempt0.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif

	cin >> N;
	
    
    
rep(i,N){    
    char s1;
	char num[4][4];
    int x,o,t;
    bool xflag = 0;
    bool oflag = 0;
    
    rep(i,4)
    rep(j,4)
    {
      cin>>s1;
      num[i][j] = s1;
    }    
    
    //row wise
    rep(i,4)
    {
    x=o=t=0;
    rep(j,4)
    {
      if(num[i][j] == 'X')       x++; 
      else if (num[i][j] == 'O') o++;
      else if (num[i][j] == 'T') t++;
    }
    
    if      (x == 4)             { xflag = 1; }
    else if (x == 3 && t == 1)   { xflag = 1; }
    else if (o == 4)             { oflag = 1; }
    else if (o == 3 && t == 1)   { oflag = 1; }
    }
    
    rep(i,4)
    {
    x=o=t=0;
    rep(j,4)
    {
      if(num[j][i] == 'X')       x++; 
      else if (num[j][i] == 'O') o++;
      else if (num[j][i] == 'T') t++;
    }
    
    if      (x == 4)             { xflag = 1; }
    else if (x == 3 && t == 1)   { xflag = 1; }
    else if (o == 4)             { oflag = 1; }
    else if (o == 3 && t == 1)   { oflag = 1; }
    }
    
    // left-diagonal
    x=o=t=0;
    rep(i,4)
    {
      if(num[i][i] == 'X') x++; 
      else if (num[i][i] == 'O') o++;
      else if (num[i][i] == 'T') t++;
      
     if      (x == 4)             {  xflag = 1; }
     else if (x == 3 && t == 1)   {  xflag = 1; }
     else if (o == 4)             {  oflag = 1; }
     else if (o == 3 && t == 1)   {  oflag = 1; }
    }
    
    // right diagonal
    x=o=t=0;
    rep(i,4)
    {
      if(num[i][3-i] == 'X') x++; 
      else if (num[i][3-i] == 'O') o++;
      else if (num[i][3-i] == 'T') t++;
      
     if      (x == 4)             {  xflag = 1; }
     else if (x == 3 && t == 1)   {  xflag = 1; }
     else if (o == 4)             {  oflag = 1; }
     else if (o == 3 && t == 1)   {  oflag = 1; }
    }
    
    
    int found = 0;
    rep(i,4)
    rep(j,4)
    {
      if(num[i][j] == '.') 
       found = 1;
    } 
    
    if(xflag) 
    cout<<"Case #"<<i+1<<": X won\n";
    
    else if(oflag) 
    cout<<"Case #"<<i+1<<": O won\n";
    
    else if(xflag && oflag) 
    cout<<"Case #"<<i+1<<": Draw\n";
    
    else if(found) 
    cout<<"Case #"<<i+1<<": Game has not completed\n";
    
    else      
    cout<<"Case #"<<i+1<<": Draw\n";
    
   // cin>>s1; cout<<s1;
}    
    
    	
    //getline(cin,s1);
   
    
   // cout<<s1;	
    
//	string s1;
//	getline(cin,s1);
//	rep2(nn,1,N+1) {
//		vs v;
//		string s;
//		getline(cin,s1);
//		ss S(s1);
//		while(S>>s)
//			v.pb(s);
//		reverse(all(v));
//		printf("Case #%d:", nn);
//		rep(i,v.sz)
//			cout<<" "<<v[i];
//		cout<<endl;
//	}
	return 0;
}
