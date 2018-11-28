
//IamAwesome
#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <iterator>
#include <set>
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstring>
#include <string>
#include <queue>
#include <stack>
#include <list>
#include <sstream>
#include <ctype.h>
#include <utility>
#include <cstdlib>
#include <functional>
#include <numeric>


using namespace std;

#define LL long long
#define linf 998877665544332211ll
#define inf 987654321ll
#define MOD 1000000007ll
#define ADD(v) accumulate(v.begin(),v.end(), 0)
#define PRO(v) accumulate(v.begin(),v.end(), 1,multiplies <int>())
LL POS(LL x) { if (x > 0)  return x; else return 0; }
#define maxe(v) max_element(v.begin(),v.end())
#define mine(v) min_element(v.begin(),v.end())
#define rep(k,a,b) for(int k=(a); k < (b); ++k)
#define per(k,a,b) for(int k=(b-1); k >= (a); --k)
#define repg(k,ctnr) for(auto k=ctnr.begin();k!=ctnr.end();k++)
#define all(ctnr) (ctnr).begin(),(ctnr).end()
//gcd
inline int gcd(int a, int b) { return b ? gcd(b, a%b) : a; }

struct ysh {
	long long z, y, x;
	ysh() {}
	ysh(long long z, long long y, long long x) : z(z), y(y), x(x) {}
	ysh operator + (const ysh &p) const { return ysh(z + p.z, y + p.y, x + p.x); }
	ysh operator - (const ysh &p)  const { return ysh(z - p.z, y - p.y, x - p.x); }
	ysh operator * (long long con)     const { return ysh(z*con, y*con, x*con); }
	ysh operator / (long long con)     const { return ysh(z / con, y / con, x / con); }
	bool operator<(const ysh &rhs) const { return make_pair(z, make_pair(y, x)) < make_pair(rhs.z, make_pair(rhs.y, rhs.x)); }
	bool operator==(const ysh &rhs) const { return make_pair(z, make_pair(y, x)) == make_pair(rhs.z, make_pair(rhs.y, rhs.x)); }
};
int dx[] = { 1, 0, -1, 0, 1, 1, -1, -1 };
int dy[] = { 0, 1, 0, -1, 1, -1, 1, -1 };


//conversion functions
string atob(const int a) {
	stringstream os;
	string b;
	os << a;
	os >> b;
	return b;
}

long long atob(const string a) {
	stringstream os;
	long long b;
	os << a;
	os >> b;
	return b;
}

bool chek(LL q1){
	LL pp= 1;
	for (int i = 1; i <= 20; i++){
		if (pp == q1){
			return true;
		}
		else if (pp > q1){
			return false;
		}
		pp = pp * 2;
	}
}

int chek2(LL q1){
	LL pp = 1;
	for (int i = 1; i <= 20; i++){
		if (pp == q1){
			return i;
		}
		pp = pp * 2;
	}
}

int main() {
	int t;
	cin >> t;
	for (int g = 1; g <= t; g++){
		LL n, l;
		LL sm, cnt, mx, mn;
		LL ans = 0;
		LL p1, q1;
		string s;
		cin >> s;
		l = s.size();
		string p, q;
		int flag = 0;
		rep(i, 0, l){
			if (s[i] == '/'){
				flag = 1;
				continue;
			}
			if (flag == 0)p.push_back(s[i]);
			else q.push_back(s[i]);
		}
		
		p1 = atob(p);
		q1 = atob(q);
		LL gc = gcd(p1, q1);
		p1 = p1 / gc;
		q1 = q1 / gc;
		//cout << p1 << " " << q1 << endl;
		if (!chek(q1)){
			cout << "Case #" << g << ": " << "impossible" << endl;
			continue;
		}
		q1 = q1 / 2;
		if (p1 > q1){
			cout << "Case #" << g << ": " << 1 << endl;
			continue;
		}
		if (p1 == 1){
			ans = chek2(q1);
			cout << "Case #" << g << ": " << ans << endl;
			continue;
		}
		else{
			int c = 1;
			while (1){
				//cout << c << endl;
				if (p1-c>=1 && q1 % (p1 - c) == 0){
					gc = gcd((p1-c), q1);
					p1 = (p1-c) / gc;
					q1 = q1 / gc;
					break;
				}
				c++;
				if (c > q1)break;
			}
			//cout << p1 << " " << q1 << endl;
			ans =chek2(q1);
			cout << "Case #" << g << ": " << ans << endl;
			continue;
		}
	}
	return 0;
}