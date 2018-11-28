#include<iostream>
#include<stack>
#include<queue>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<set>
#include<string>
#include<cstring>
#include<map>
#include<numeric>
#include<sstream>
#include<cmath>
using namespace std;
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define pb push_back
#define f(i,x,y) for(int i = x; i<y; i++ )
#define FORV(it,A) for(vector<int>::iterator it = A.begin(); it!= A.end(); it++)
#define FORS(it,A) for(set<int>::iterator it = A.begin(); it!= A.end(); it++)
#define quad(x) (x) * (x)
#define mp make_pair
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second
typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;
#define mod 1000000007




#define N 20000


int pos[N];
int v[N], n;

int solve (int ele){
	if (ele == n-1) return 0;
	int cnt = 0;
	f (i, 0, pos[ele]){
		if (v[i] > ele) cnt++;
	}
	int cnt2 = 0;
	f (i, pos[ele]+1, n){
		if (v[i] > ele) cnt2++;
	}
	return min(cnt, cnt2) + solve(ele+1);

}




int main (){
	int t; cin >> t;
	f (tt, 1, t+1){
		cin >> n;
		f (i, 0, n) cin >> v[i];
		set <int> S;
		map <int, int> mapa;
		
		f (i, 0, n) S.insert(v[i]);
		int cnt = 0;
		FORS (it, S){
			mapa[*it] = cnt++;
		}

		f (i, 0, n) v[i] = mapa[v[i]], pos[v[i]] = i;

		printf("Case #%d: %d\n", tt, solve(0));

	}
	return 0;
}
