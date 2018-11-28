#include<map>
#include<set>
#include<ctime>
#include<cmath>
#include<queue>
#include<stack>
#include<bitset>
#include<vector>
#include<cstdio>
#include<string>
#include<cassert>
#include<cstring>
#include<numeric>
#include<sstream>
#include<iterator>
#include<iostream>
#include<algorithm>
using namespace std;
typedef long long LL;
#define MM(a,x) memset(a, x, sizeof(a))
#define P(x) cout<<#x<<" = "<<x<<endl;
#define P2(x,y) cout<<#x<<" = "<<x<<", "<<#y<<" = "<<y<<endl;
#define PV(a,n) for(int i=0;i<n;i++) cout<<#a<<"[" << i <<"] = "<<a[i]<<endl;
#define TM(a,b) cout<<#a<<"->"<<#b<<": "<<1.*(b-a)/CLOCKS_PER_SEC<<"s\n";

bool isp(LL n) {
	vector<int> v;
	while(n) {v.push_back(n % 10); n /= 10;}
	n = v.size();
	for(int i = 0; i + i < n; i++) if(v[i] != v[n - 1 - i]) return 0;
	return 1;
}

class String {
public:
	String(string str = string()) {s = str;}
	bool operator < (const String& o) const {
		if(s.length() != o.s.length())
			return s.length() < o.s.length();
		else return
			    s < o.s;
	}
	string s;
};

vector<String> vs;
vector<string> gen;

string operator * (const string& a, const string& b) {
	int *mu = new int[a.length() + b.length()];
	memset(mu, 0, sizeof(int) * (a.length() + b.length()));

	for(int i = 0; i < a.length(); i++)             //将数字两两相乘
		for(int j = 0; j < b.length(); j++)
			mu[i + j + 1] += (a[i] - '0') * (b[j] - '0');

	for(int i = a.length() + b.length() - 1; i > 0; i--) { //进位操作
		if(mu[i] > 9) {
			mu[i - 1] += mu[i] / 10;
			mu[i] %= 10;
		}
	}
	//后面同加法
	char *c = new char[a.length() + b.length()];
	int i = 0, j = 0;

	while(mu[i] == 0) i++;
	while(i < a.length() + b.length()) c[j++] = mu[i++] + '0';
	c[j] = '\0';
	if(c[0] == '\0') {c[1] = '\0'; c[0] = '0';}
	free(mu);
	string s(c);
	return s;
}

bool palindrome(string p) {
	string q = p;
	reverse(q.begin(), q.end());
	return p == q;
}

void dfs(int cur, string p, int sum) {
	if(sum > 5) return;
	if(cur == 31) return;
	vs.push_back(String(p));
	dfs(cur + 1, p + '0', sum);
	dfs(cur + 1, p + '1', sum + 1);
	dfs(cur + 1, p + '2', sum + 4);
}

void init() {
	dfs(1, "1", 1);
	dfs(1, "2", 4);
	sort(vs.begin(), vs.end());
	
	//for(int i = 0; i < 25; i++) {
	//	cout << i << "=" << vs[i].s << endl;
	//}

	for(int i = 0; i < vs.size(); i++) {
		string& p = vs[i].s;
		string q = p;
		reverse(q.begin(), q.end());
		string t = p + q;
		if(palindrome(t) && palindrome(t * t)) gen.push_back(t * t);
		for(int j = 0; j < 3; j++) {
			string t = p + char('0' + j) + q;
			if(palindrome(t) && palindrome(t * t)) gen.push_back(t * t);
		}
	}
	sort(gen.begin(), gen.end());
	gen.resize(unique(gen.begin(), gen.end()) - gen.begin());
	vs.clear();
	for(int i = 0; i < gen.size(); i++)vs.push_back(gen[i]);

	vs.push_back(string("1"));
	vs.push_back(string("4"));
	vs.push_back(string("9"));
	sort(vs.begin(), vs.end());
}

int f(string A) {
	int r = lower_bound(vs.begin(), vs.end(), String(A)) - vs.begin();
	if(vs[r].s == A) r++;
	//P(r);
	return r;
}

string dec(string A) {
	reverse(A.begin(), A.end());
	for(int i = 0; i < A.length(); i++) {
		if(A[i] > '0') {
			A[i]--;
			for(int j = 0; j < i; j++) A[j] = '9';
			break;
		}
	}
	reverse(A.begin(), A.end());
	for(int i = 0; i < A.length(); i++) if(A[i] != '0') return A.substr(i);
	return "0";
}

int main() {
	string A, B;
	init();
//	for(int i = 0; i < 25; i++) {
//		cout << i << "=" << vs[i].s << endl;
//	}
	int T;
	cin >> T;
	for(int i = 1; i <= T; i++) {
		cin >> A >> B;
		LL r = f(B) - f(dec(A));
		cout << "Case #" << i << ": " << r << endl;
	}
	return 0;
}

