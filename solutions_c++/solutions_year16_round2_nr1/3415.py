//#include <bits/stdc++.h>
//using namespace std;
//typedef long long int ll;
//typedef vector<int> vi;
//typedef vector<ll> vll;
//typedef pair<int, int> ii;
//typedef vector<ii> vii;
//#define sc(x) scanf("%d", &x)
//#define scl(y) scanf("%lld", &y)
//#define loop(i,s,e) for(int i=s ; i<e ; i++)
//#define rep(i,s,e) for(int i=s ; i>=e ; i--)
//#define INF 1000000
//#define MOD 1000000007
//#define f first
//#define s second
//#define EPS 1e-7
//#define Rd freopen("in.txt", "r", stdin)
//#define Wr freopen("out.txt", "w", stdout)
//#define PS push_back
//#define M_PI           3.14159265358979323846  /* pi */
//
//string c, j;
//vi vec_c, vec_j;
//void gen_c(int i, int num) {
//	if (i == (int) c.size()) {
//		vec_c.push_back(num);
//		return;
//	}
//	int ten = round(pow(10, c.size() - i - 1));
//	if (c[i] != '?') {
//		gen_c(i + 1, num + int((c[i] - '0') * ten));
//	} else {
//		loop(j,0,10)
//		{
//			gen_c(i + 1, num + (j * ten));
//		}
//	}
//}
//void gen_j(int i, int num) {
//	if (i == (int) j.size()) {
//		vec_j.push_back(num);
//		return;
//	}
//	int ten = round(pow(10, j.size() - i - 1));
//	if (j[i] != '?') {
//		gen_j(i + 1, num + int((j[i] - '0') * ten));
//	} else {
//		loop(j,0,10)
//		{
//			gen_j(i + 1, num + (j * ten));
//		}
//	}
//}
//int main() {
//	Rd;
//	Wr;
//	int T;
//	sc(T);
//	loop(t,0,T)
//	{
//		cin >> c >> j;
//		vec_c.clear();
//		vec_j.clear();
//		gen_c(0, 0);
//		gen_j(0, 0);
//		sort(vec_c.begin(), vec_c.end());
//		sort(vec_j.begin(), vec_j.end());
//		int mn = INF;
//		int idx1 = 0, idx2 = 0;
//		loop(i,0,vec_c.size())
//		{
//			loop(j,0,vec_j.size())
//			{
//				if (abs(vec_c[i] - vec_j[j]) < mn) {
//					mn = abs(vec_c[i] - vec_j[j]);
//					idx1 = i;
//					idx2 = j;
//				}
//			}
//		}
//		stringstream ss;
//		ss << vec_c[idx1];
//		string s1 = ss.str();
//		while (s1.size() < c.size()) {
//			s1 = ('0' + s1);
//		}
//		ss.clear();
//		ss.str("");
//		ss << vec_j[idx2];
//		string s2 = ss.str();
//		while (s2.size() < j.size()) {
//			s2 = ('0' + s2);
//		}
//		printf("Case #%d: %s %s\n", t + 1, s1.c_str(), s2.c_str());
//	}
//	return 0;
//}

// A

#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
#define sc(x) scanf("%d", &x)
#define scl(y) scanf("%lld", &y)
#define loop(i,s,e) for(int i=s ; i<e ; i++)
#define rep(i,s,e) for(int i=s ; i>=e ; i--)
#define INF INT_MAX
#define MOD 1000000007
#define f first
#define s second
#define EPS 1e-7
#define Rd freopen("in.txt", "r", stdin)
#define Wr freopen("out.txt", "w", stdout)
#define PS push_back
#define M_PI           3.14159265358979323846  /* pi */

map<char, int> Map;
string numbers[] = { "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX",
		"SEVEN", "EIGHT", "NINE" };

char intNum(string s) {
	loop(i,0,10)
	{
		if (s == numbers[i])
			return (i + '0');
	}
	return 0;
}
bool has(int x) {
	string word = numbers[x];
	loop(i,0,word.size())
	{
		if (Map[word[i]] <= 0)
			return false;
	}
	return true;
}

void exec(int x) {
	string word = numbers[x];
	loop(i,0,word.size())
	{
		Map[word[i]]--;
	}
}

void doback(int x) {
	string word = numbers[x];
	loop(i,0,word.size())
	{
		Map[word[i]]++;
	}
}

string ans = "";
bool solve(int st, int rest) {
	if (rest < 0)
		return false;
	if (rest == 0)
		return true;
	loop(i,st,10)
	{
		if (has(i)) {
			exec(i);
			if (solve(i, rest - numbers[i].size())) {
				ans = intNum(numbers[i]) + ans;
				return true;
			}
			doback(i);
		}
	}
	return false;
}

int main() {
	Rd;
	Wr;
	int T;
	sc(T);
	loop(t,0,T)
	{
		string s;
		cin >> s;
		loop(i,0,s.size())
		{
			Map[s[i]]++;
		}
		ans = "";
		if (solve(0, s.size()))
			printf("Case #%d: %s\n", t + 1, ans.c_str());
	}

	return 0;
}
