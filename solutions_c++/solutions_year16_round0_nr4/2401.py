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

int del[20];


int prime(ll k){
	for (ll i = 2; i * i <= k; i++){
		if (k % i == 0){
			return i;
		}
	}
	return 0;
}

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(0);
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++){
		ll k, c, s;
		cin >> k >> c >> s;
	//	ll tmp = pow(k, c);
		print(i);
		for (int j = 1; j <= k; j++){
			cout << j << " ";
		}
		cout << "\n";
	}
	return 0;
}