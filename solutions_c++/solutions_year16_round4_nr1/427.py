/*
ID: ashish1610
PROG:
LANG: C++
*/
#include<bits/stdc++.h>
using namespace std;
#define ll				long long int
#define MOD				1000000007
#define si(a)			scanf("%d", &a)
#define sl(a)			scanf("%lld", &a)
#define pi(a)			printf("%d", a)
#define pl(a)			printf("%lld", a)
#define pn 				printf("\n")
ll pow_mod(ll a, ll b) {
	ll res = 1;
	while(b) {
		if(b & 1) {
			res = (res * a) % MOD;
		}
		a = (a * a) % MOD;
		b >>= 1;
	}
	return res;
}
string get(string str) {
	for(int i = 1; i < (int)(str.size()); i += i) {
		for(int j = 0; j < (int)(str.size()); j += 2 * i) {
			bool flag = false;
			for(int k = 0; k < i; ++k) {
				if(str[j + k] < str[j + k + i]) {
					break;
				}
				if(str[j + k] > str[j + k + i]) {
					flag = true;
					break;
				}
			}
			if(flag) {
				for(int k = 0; k < i; ++k) {
					swap(str[j + k], str[j + k + i]);
				}
			}
		}
	}
	return str;
}
pair < int, string > func(char st, int n, int r, int p, int s) {
	queue < pair < char, int > > q;
	int r1 = r, p1 = p, s1 = s;
	q.push(make_pair(st, n));
	string res;
	while(!q.empty()) {
		pair < char, int > it = q.front();
		q.pop();
		if(!it.second) {
			res += it.first;
			if(it.first == 'R') {
				--r1;
			} else if(it.first == 'P') {
				--p1;
			} else if(it.first == 'S') {
				--s1;
			}
		} else {
			if(it.first == 'R') {
				q.push(make_pair('R', it.second - 1));
				q.push(make_pair('S', it.second - 1));
			} else if(it.first == 'S') {
				q.push(make_pair('P', it.second - 1));
				q.push(make_pair('S', it.second - 1));
			} else if(it.first == 'P') {
				q.push(make_pair('P', it.second - 1));
				q.push(make_pair('R', it.second - 1));
			}
		}
	}
	if((!r1) && (!p1) && (!s1)) {
		return make_pair(1, get(res));
	} else {
		return make_pair(0, "#");
	}
}
bool check(string str) {
	bool found = true;
	string tmp = str;
	while((int)(tmp.length()) != 1) {
		string new_str = "";
		bool flag = false;
		for(int i = 0; i < (int)(tmp.length()); i += 2) {
			if(tmp[i] == 'R' && tmp[i + 1] == 'P') {
				new_str += 'P';
			} else if(tmp[i] == 'R' && tmp[i + 1] == 'S') {
				new_str += 'R';
			} else if(tmp[i] == 'P' && tmp[i + 1] == 'S') {
				new_str += 'S';
			} else if(tmp[i] == 'P' && tmp[i + 1] == 'R') {
				new_str += 'P';
			} else if(tmp[i] == 'S' && tmp[i + 1] == 'R') {
				new_str += 'R';
			} else if(tmp[i] == 'S' && tmp[i + 1] == 'P') {
				new_str += 'S';
			} else if(tmp[i] == tmp[i + 1]) {
				flag = true;
				break;
			}
		}
		if(flag) {
			found = false;
			break;
		} else {
			tmp = new_str;
		}
	}
	return found;
}
int main() {
	int t;
	cin >> t;
	for(int tcase = 1; tcase <= t; ++tcase) {
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		string res = "#";
		vector < string > v;
		pair < int,  string > p1 = func('R', n, r, p, s);
		if(p1.first) {
			v.push_back(p1.second);
		}
		p1 = func('P', n, r, p, s);
		if(p1.first) {
			v.push_back(p1.second);
		}
		p1 = func('S', n, r, p, s);
		if(p1.first) {
			v.push_back(p1.second);
		}
		if(!v.empty()) {
			sort(v.begin(), v.end());
			res = v[0];
		}
		cout << "Case #" << tcase << ": ";
		if(res[0] == '#') {
			cout << "IMPOSSIBLE\n";
		} else {
			if(!check(res)) {
				assert(false);
			}
			int p1 = 0, r1 = 0, s1 = 0;
			assert((int)(res.length()) == r + p + s);
			for(int i = 0; i < (int)(res.length()); ++i) {
				if(res[i] == 'P') {
					p1 += 1;
				} else if(res[i] == 'R') {
					r1 += 1;
				} else {
					s1 += 1;
				}
			}
			assert(p1 == p);
			assert(r1 == r);
			assert(s1 == s);
			cout << res << endl;
		}
	}
	return 0;
}