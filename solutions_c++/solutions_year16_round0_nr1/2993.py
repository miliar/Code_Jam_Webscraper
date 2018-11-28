#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<fstream>
#include<cstdlib>
#include<cstdio>
#include<map>
#include<set>
#include<algorithm>
#include<cmath>
#include<iomanip>
#include<queue>
#include<stack>
#include<vector>
#include<string>
//#include<unordered_set>
using namespace std;
#define mp make_pair
#define pb push_back
typedef long long ll;
typedef long double ld;

void print(int tst){
	cout << "Case #" << tst << ": ";
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(0);
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++){
		vector <int> used(10, 0);
		ll x;
		cin >> x;
		if (x == 0){
			print(i);
			cout << "INSOMNIA" << "\n";
			continue;
		}
		int cnt = 0;
		int c = 0;
		for (ll j = x; j <= 1e18; j += x){
			ll cur = j;
			cnt++;
			while (cur){
				c += 1 - used[cur % 10];
				used[cur % 10] = 1;
				cur /= 10;
			}
			if (c == 10){
				break;
			}
		}
		print(i);
		cout << cnt * x << "\n";
	}
	return 0;
}