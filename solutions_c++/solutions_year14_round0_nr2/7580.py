#include <bits/stdc++.h>
#define f(i,x,y) for (int i = x; i < y; i++)
#define fd(i,x,y) for(int i = x; i>= y; i--)
#define FOR(it,A) for(typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define vint vector<int>
#define ll long long
#define clr(A,x) memset(A, x, sizeof A)
#define pb push_back
#define pii pair<int,int>
#define mp make_pair
#define fst first
#define snd second
#define ones(x) __builtin_popcount(x)
#define cua(x) (x)*(x)
#define eps (1e-9)
#define oo (1<<30)
#define OO (1LL<<60)
#define debug(x) cout <<#x << " = " << x << endl
#define adebug(x,n) cout <<#x<<endl; f(i,0,n)cout<<x[i]<<char(i+1==n?10:32)
#define mdebug(x,m,n) cout <<#x<<endl; f(i,0,m)f(j,0,n)cout<<x[i][j]<<char(j+1==n?10:32)
#define sz(a) int((a).size()) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 
#define N 1005
using namespace std;
template<class T> inline void mini(T &a,T b){if(b<a) a=b;}
template<class T> inline void maxi(T &a,T b){if(b>a) a=b;}

main(){
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	f(C,0,t){
		double c,f,x;
		cin>>c>>f>>x;
		double totsec = 0.0;
		double incrate = 2.0;
		bool better=true;
		while(better){
			double est_sec = x/incrate;
			double est2_sec = c/incrate;
			double rest_est2 = x/(incrate+f);
			double tot2_sec = est2_sec + rest_est2;
			if(tot2_sec - est_sec< eps){
				incrate = incrate +f;
				totsec += est2_sec;
			}
			else{
				better=false;
				totsec+=est_sec;
			}
		}
		printf("Case #%d: %.7lf\n",C+1,totsec);
	}
}
