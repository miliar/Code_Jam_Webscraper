#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <fstream>
#include <iomanip>
#include <set>
#include <cstdio>
#include <cstring>
#include <stack>
#include <string>
#include <map>
#include <vector>
#include <queue>
#include <deque>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <bitset>
#include <ctime>
#include <list>
#include <functional>
using namespace std;
#define mp make_pair
#define ull unsigned long long
#define ll long long
#define mod1 (ll)1000000009
#define mod (ll)1000000007
#define inf (ll)1600000016000000000
#define mpi acos(-1.0)
#define M_E (double)2.71828182846
#pragma comment(linker, "/STACK:1000000000")

ll prime(ll n){
	for (ll i = 2; i * i <= n; ++i)
		if (n % i == 0)
			return i;
	return 0;
}

void inc(string &s){
	s[s.length() - 2]++;
	for (int i = s.length() - 2; i; --i)
		if (s[i] == '2'){
			s[i] = '0';
			s[i - 1]++;
 		}
}

ll conv(string &s, int base){
	ll cur = 0;
	for (int i = 0; i < s.length(); ++i){
		cur = cur * base + s[i] - '0';
	}
	return cur;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	//freopen("B-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int n, k;
	cin >> n;
	cin >> n >> k;
	cout << "Case #1:\n";
	string s = "1";
	for (int i = 0; i < n - 2; ++i)
		s.push_back('0');
	s.push_back('1');
	while (k){
		int a = 0;
		for (int i = 2; i <= 10; ++i){
			//cout << conv(s, i) << ' ';
			a += !prime(conv(s, i));
			if (a)
				break;
		}
		//cout << '\n';
		if (!a){
			--k;
			cout << s << ' ';
			for (int i = 2; i <= 10; ++i)
				cout << prime(conv(s, i)) << ' ';
			cout << '\n';
		}
		inc(s);
	}
	//system("pause");
	return 0;
}