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
#include <fstream>

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
typedef unsigned  long long int ll;
typedef long double ld;
typedef complex<double> point;
typedef pair<point, point> segment;
typedef pair<double, point> circle;
typedef vector<point> polygon;

const int oo = (int) 1e9;
const double PI = 2 * acos(0);
const double eps = 1e-9;

#define SMALL
//#define LARGE

int PS(long n)
{
    int h = n & 0xF;
    if (h > 9)
        return 0;
    if ( h != 2 && h != 3 && h != 5 && h != 6 && h != 7 && h != 8 )
    {

        int t = (int) floor( sqrt((double) n));
            return t*t == n;
    }
    return 0;
}

long sr( long  number )
{
  long i;
  long x2, y;
  const float threehalfs = 1.5F;

  x2 = number * 0.5F;
  y  = number;
  i  = * ( long * ) &y;  // evil floating point bit level hacking
  i  = 0x5f3759df - ( i >> 1 ); // wtf?
  y  = * ( float * ) &i;
  y  = y * ( threehalfs - ( x2 * y * y ) ); // 1st iteration
  // y  = y * ( threehalfs - ( x2 * y * y ) ); // 2nd iteration, this can be removed
  return y;
}

bool isPal(long num){
  long n = num/1;
  long rev = 0;
 while (num > 0)
 {
     long  dig = num % 10;
      rev = rev * 10 + dig;
      num = num / 10;
 }
 return n==rev;
}

int main() {
int n;
#ifdef SMALL
	freopen("C-small-attempt1.in","rt",stdin);
	freopen("C-small1.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
int l,r;
cin>>n;
rep(i,n){
	int c=0;
	  cin>>l>>r;
	  cout<<"Case #"<<i+1<<": ";
	  for(int i=l;i<=r;i++){
			int r=sqrt(i);
        if(PS(i)&&isPal(i)&&isPal(r))
			{c+=1; //cout<<" "<<i<<" ";
			}
	 }
	 cout<<c<<endl;
}
}
