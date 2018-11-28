#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
#define sc(x) scanf("%d", &x)
#define scl(x) scanf("%I64d", &x)
#define loop(i,s,e) for(int i=s ; i<e ; i++)
#define rep(i,s,e) for(int i=s ; i>=e ; i--)
#define INF 1000000
#define MOD 1000000007
#define f first
#define s second
#define EPS 1e-7
#define Rd freopen("in.txt", "r", stdin)
#define Wr freopen("out.txt", "w", stdout)
#define PS push_back
#define M_PI           3.14159265358979323846  /* pi */

int main() {
	Rd;
	Wr;
	int T, k, c, s;
	sc(T);
	loop(t,0,T)
	{
		printf("Case #%d:", t + 1);
		sc(k);
		sc(c);
		sc(s);
		if ((c == 1 && s < k) || (c > 1 && s < k - 1))
			printf(" IMPOSSIBLE\n");
		else {
			loop(i,0,k)
			{
				printf(" %d", i + 1);
			}
			printf("\n");
		}
	}
	return 0;
}

//int k, c;
//string s;
//void gen_seq(string s) {
//	string res = s;
//	string org = s;
//	string g;
//	g.assign(s.size(), 'G');
//	loop(i,1,c)
//	{
//		s = res;
//		res = "";
//		loop(i,0,s.size())
//		{
//			if (s[i] == 'L')
//				res += org;
//			else
//				res += g;
//		}
//	}
//	printf("%s\n", res.c_str());
//}
//void gen(int n) {
//	if (n == 0) {
//		printf("%s: ", s.c_str());
//		gen_seq(s);
//		return;
//	}
//	s += 'L';
//	gen(n - 1);
//	s.erase(s.end() - 1);
//	s += 'G';
//	gen(n - 1);
//	s.erase(s.end() - 1);
//}
//int main() {
//	Rd;
//	//	Wr;
//	cin >> k >> c;
//	s = "";
//	gen(k);
//	return 0;
//}
