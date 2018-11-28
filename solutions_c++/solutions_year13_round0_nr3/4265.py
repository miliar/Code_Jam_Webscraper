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
#define quad(x) ((x) * (x))
#define mp make_pair
#define clr(x, y) memset(x, y, sizeof x)
#define fst first
#define snd second
#define eps 1e-7
typedef pair<int, int> pii;
typedef long long ll;
typedef long double ld;


	
ll v[39] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004};	
	
int main() {
	/*int cont = 0;
	for (ll i = 1; i <= 10000000; i++) {
		if (palindromo(i) && palindromo(i*i)) {
			printf("%lld, ", i*i);
			cont++;
		}
	}
	printf("cont=%d\n", cont);*/
	int n; cin >> n;
	ll a, b;
	for (int caso = 1; caso <= n; caso++) {
		int cont = 0;
		scanf("%lld %lld", &a, &b);
		for (int i = 0; i < 39; i++) if (a <= v[i] && v[i] <= b) cont++;
		printf("Case #%d: %d\n", caso, cont);
	
	}	
	return 0;
}
		

	
