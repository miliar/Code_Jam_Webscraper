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




double C, F, X;

int main (){
	int tt = 1;
	int t; cin >> t;
	while (t--){
		cin >> C >> F >> X;
		double at = 2.;
		double ans = X/at;
		double t = 0;
		while (1){
			double p = C/at;
			t += p;
			at += F;
			double ansp = t+X/at;
			if (ansp > ans) break;
			ans = ansp;

		}

		printf("Case #%d: %.10f\n", tt++, ans);
		
	}
	return 0;
}

