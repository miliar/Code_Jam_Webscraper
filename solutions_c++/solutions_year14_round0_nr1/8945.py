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
	int tc;
	scanf("%d", &tc);
	int row1, row2;
	int mat[17], a1[4][4], a2[4][4];
	int caso = 0;
	while(tc--){
		caso++;
		clr(mat,0);
		scanf("%d", &row1);
		row1--;
		f(i,0,4) f(j,0,4) scanf("%d", &a1[i][j]);
		f(i,0,4) mat[a1[row1][i]]++;
		scanf("%d", &row2);
		row2--;
		f(i,0,4) f(j,0,4) scanf("%d", &a2[i][j]);
		f(i,0,4) mat[a2[row2][i]]++;
		int cont = 0;
		int res=-1;
		f(i,1,17){
			if(mat[i]==2){
				cont++;
				res=i;
			}
		}
		if(res==-1){
			printf("Case #%d: Volunteer cheated!\n", caso);
		}
		else{
			if(cont>1) printf("Case #%d: Bad magician!\n", caso);
			else printf("Case #%d: %d\n", caso, res);
		} 

	}

}
