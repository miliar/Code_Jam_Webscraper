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



int M[2][5][5];

int main (){
	int tt = 1;
	int t; cin >> t;
	while (t--){
		int a, b;
		cin >> a;
		a--;
		f (i, 0, 4) f (j, 0, 4) cin >> M[0][i][j];
		cin >> b; b--;
		f (i, 0, 4) f (j, 0, 4) cin >> M[1][i][j];
		vector <int> ans;
		f(k, 1, 17){
			int acho = 0;
			f (i, 0, 4) f (j, 0, 4) if (M[0][i][j] == k && i == a) acho++;
			f (i, 0, 4) f (j, 0, 4) if (M[1][i][j] == k && i == b) acho++;
			if (acho == 2) ans.pb(k);
		}
		printf("Case #%d: ", tt++);
		if (ans.size() == 0) cout << "Volunteer cheated!" << endl;
		else if (ans.size() != 1) cout << "Bad magician!" << endl;
		else cout << ans[0] << endl;
	}
	return 0;
}

