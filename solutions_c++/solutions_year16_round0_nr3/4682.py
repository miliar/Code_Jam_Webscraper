#define _CRT_SECURE_NO_WARNINGS
#include <cstring>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <numeric>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <hash_map>
#include <fstream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>
#include <climits>
#include <cctype>
#include <bitset>

#define PI 3.14159265359
#define all(v) v.begin(),v.end()
#define sortva(v) sort(all(v))
#define sortvd(v) sort(v.rbegin(),v.rend())
#define sortaa(a,n) sort(a,a+n)
#define sortad(a,n) sort(a,a+n),reverse(a,a+n)
#define sfi1(v) scanf("%d",&v)
#define sfi2(v1,v2) scanf("%d %d",&v1,&v2)
#define sfi3(v1,v2,v3) scanf("%d %d %d",&v1,&v2,&v3)
#define sfll1(v) scanf("%I64d",&v);
#define sfll2(v1,v2) scanf("%I64d %I64d",&v1,&v2)
#define sfll3(v1,v2,v3) scanf("%I64d %I64d %I64d",&v1,&v2,&v3)
#define pfi1(v) printf("%d ",v)
#define pfi2(v1,v2) printf("%d %d ",v1,v2)
#define pfi3(v1,v2,v3) printf("%d %d %d ",v1,v2,v3)
#define pfll1(v) printf("%I64d ",v)
#define pfll2(v1,v2) printf("%I64d %I64d ",v1,v2)
#define pfll3(v1,v2,v3) printf("%I64d %I64d %I64d ",v1,v2,v3)
#define ndl puts("")
#define SS stringstream
typedef long long ll;
using namespace std;
void openfile() {
	cout << fixed << setprecision(15);
	#ifndef ONLINE_JUDGE 
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
	#endif
}

string all[100000];
int size;


void generate(string s) {
	string comp(s.size(), '1');
	all[size++] = s;
	while (s != comp) {
		int i = s.size() - 1;
		if (s[i] == '0')
			s[i] = '1';
		else {
			s[i] = '0';
			for (int x = i - 1; x >= 0; x--) {
				if (s[x] == '0') {
					s[x] = '1';
					s[i] = '1';
					break;
				}
				s[x] = '0';
			}
		}
		all[size++] = s;
	}
}

ll toInt(string s) {
	SS ss;
	ss << s;
	ll n;
	ss >> n;
	return n;

}
ll con(string n, int b){
	ll op = 0, k = toInt(n), p = 1, s;
	while (k) {
		s = k % 10;
		k = k / 10;
		op = op + s*p;
		p = p*b;
	}
	return op;
}

ll prime(ll n) {
	for (ll i = 2LL; i * i <= n; i++)
		if (n % i == 0)
			return i;
	return -1LL;
}

vector<ll> check(string s) {
	vector<ll> ret;
	for (int i = 2; i <= 10; i++) {
		ll x = prime(con(s, i));
		if (x != -1)
			ret.push_back(x);
		else
			break;
	}
	return ret;
}

int main(){
	openfile();
	
	int t, n, j;
	sfi3(t, n, j);
	printf("Case #1:\n");

	string s(n, '0');
	s[0] = s[n - 1] = '1';
	generate(s);

	int f = 0;
	for (int i = 0; i < size && f != j; i++) {
		vector<ll> x = check(all[i]);
		if (x.size() == 9) {
			f++;
			cout << all[i] << " ";
			for (int j = 0; j < 9; j++) {
				if (j == 8)
					cout << x[j];
				else
					cout << x[j] << " ";
			}
			if(f != j ) ndl;
		}
	}

	return 0;
}