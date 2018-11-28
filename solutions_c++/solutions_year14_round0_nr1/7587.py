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
#define N 4
using namespace std;
template<class T> inline void mini(T &a,T b){if(b<a) a=b;}
template<class T> inline void maxi(T &a,T b){if(b>a) a=b;}

main(){
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	f(c,0,t){
		int a1,a2;
		int mat1[N][N],mat2[N][N],r1[N],r2[N];
		cin>>a1;
		f(i,0,N) f(j,0,N) cin>>mat1[i][j];
		cin>>a2;
		f(i,0,N) f(j,0,N) cin>>mat2[i][j];
		f(i,0,N) r1[i] = mat1[a1-1][i];
		f(i,0,N) r2[i] = mat2[a2-1][i];
		int res, cnt=0;
		f(i,0,N) f(j,0,N) if(r1[i]==r2[j]) cnt++, res=r1[i];
		printf("Case #%d: ",c+1);
		if(cnt==1) printf("%d\n", res);
		if(cnt>1) printf("Bad magician!\n");
		if(cnt==0) printf("Volunteer cheated!\n"); 
	}
}
