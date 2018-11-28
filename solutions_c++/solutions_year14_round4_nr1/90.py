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
int v[N];
multiset<int> S;
int X;
int n;
int main (){
	int t; cin >> t;
	f (tt, 1, t+1){
		cin >> n >> X;
		f (i, 0, n){
			int x; cin >> x;
			v[i] = x;
		}
		
		sort (v, v+n);


		int ans = 0;
		int i = 0, j = n-1;
		while (i <= j){
			if (i == j) ans++, i++;
			else if (v[i]+v[j] <= X){
				ans++; i++, j--;
			}
			else ans++, j--;
		}
		printf("Case #%d: %d\n", tt, ans);

	}
	return 0;
}
