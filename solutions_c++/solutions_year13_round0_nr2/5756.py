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



#define SMALL
//#define LARGE

int main() {
#ifdef SMALL
	freopen("B-small-attempt5.in","rt",stdin);
	freopen("B-small5.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("C-large.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
#endif
int t,n,m;
cin>>t;
rep(i,t)
{
	int fl=1,fr=1,fc=1;
	printf("Case #%d: ",(i+1));  // cout<<endl;

	cin>>n>>m;
	int gr[n][m];
	int mx=0;
	int res[n][m];
	rep(j,n){
	  rep(k,m)
	  {
	  	cin>>gr[j][k];
	  	if(mx<gr[j][k]) mx=gr[j][k]/1;
	  	if(gr[j][k]==2) res[j][k]=1;  //small test case only 2|1
	  	else res[j][k]=0;
	  }
	}
     if(n==1||m==1){
		printf("YES\n");
		continue;
     }
     int a=1;
     for(int j=0;j<=n-1;j++){
			int no1=0;
        for(int k=0;k<=m-1;k++){
              if(gr[j][k]!=a) break;
              if(gr[j][k]==a){
				for(int h=0;h<m;h++){
					if(gr[j][h]==a){
						no1+=1;
					}
				}
				if(no1==m){
					rep(h,m)
					   res[j][h]=1;
				}
              }
         }
     }
       a=1;
      for(int k=0;k<m;k++){
			int no1=0;
		 if(gr[0][k]!=a) {continue;}
		 else  if(gr[0][k]==a){
				for(int h=0;h<n;h++){
					if(gr[h][k]==a){
					     no1+=1;
					}
				}
				if(no1==n){
					rep(h,n){
					   res[h][k]=1;
					}
				}
              }
      }
      rep(j,n){
	    rep(k,m){
	      if(res[j][k]==0)
		  {
		  	fl=0;
		    printf("NO\n");
		  	break;
		  }
	    }
	    if(fl==0) break;
	 }
	  if(fl==1) {printf("YES\n");continue;}
	}
}

