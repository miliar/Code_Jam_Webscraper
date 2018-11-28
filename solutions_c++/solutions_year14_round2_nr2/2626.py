#include <bits/stdc++.h>
using namespace std;

#define F first
#define S second
#define oo (1<<30)
#define pb push_back
#define mp make_pair
#define bg puts("bug")
#define cl(A) A.clear()
#define pii pair<int,int>
#define sz(A) int(A.size())
#define rsz(A,B) A.resize(B)
#define pdd pair<double,double>
#define ALL(A) A.begin(),A.end()
#define RALL(A) A.rbegin(),A.rend()
#define mem(A,B) memset(A,B,sizeof A)
#define rep(A,B,C) for(int A=B;A<C;A++)
#define rep_(A,B,C) for(int A=B;A>=C;A--)
#define print(A) printf("%s = %d\n",#A,A)

typedef long long int lli;

int dx[] = {0,0,1,-1,1,-1,1,-1} , dy[] = {1,-1,0,0,1,-1,-1,1};

int main() {

#ifndef ONLINE_JUDGE
	freopen("B-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
#endif

	int t;
	scanf("%i",&t);
	rep( k , 1 , t + 1 ){
		int f , s , r;
		scanf("%i %i %i",&f,&s,&r);
		set<pii> st;
		rep ( a , 0 , f ) rep ( b , 0 , s ){
			int c = a & b;
			if ( c < r ) st.insert(mp(a,b));
		}
		cout << "Case #" << k << ": " << sz(st) << endl;
	}
	return 0;
}
