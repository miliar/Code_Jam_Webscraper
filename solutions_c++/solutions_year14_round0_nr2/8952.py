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
#define fst first
#define snd second
#define ones(x) __builtin_popcount(x)
#define cua(x) (x)*(x)
#define eps (1e-9)
#define oo (1<<30)
#define debug(x) cout <<#x << " = " << x << endl
#define adebug(x,n) cout <<#x<<endl; f(i,0,n)cout<<x[i]<<char(i+1==n?10:32)
#define mdebug(x,m,n) cout <<#x<<endl; f(i,0,m)f(j,0,n)cout<<x[i][j]<<char(j+1==n?10:32)
#define N 1005
using namespace std;
template<class T> inline void mini(T &a,T b){if(b<a) a=b;}
template<class T> inline void maxi(T &a,T b){if(b>a) a=b;}


main(){
	int tc, caso=0;
	double t1=0.0, t2=0.0, c, x, f;
	scanf("%d", &tc );
	while(tc--){
		caso++;
		t1=0.0; t2=0.0;
		scanf("%lf %lf %lf", &c, &f, &x);
		t1=x/2.0;
		double c_act = 2.0;
		while(1){
			t2 += c/c_act;
			c_act += f;
			t2 += x/c_act;
			//cout<<t2<<" "<<t1<<endl;
			if(t2>t1)	break;
			else{
				double aux = t1;
				t1=t2;
				t2-=x/c_act;
			}
		}
		printf("Case #%d: %.7lf\n", caso, t1);
	}

}
