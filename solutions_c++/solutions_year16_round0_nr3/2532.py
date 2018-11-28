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
	//freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	ios::sync_with_stdio(0);
	int base;
	cin >> base;
	int cnt = 0;
	print(1);
	cout << endl;
	for (int i = (1 << (base - 1)) + 3; i < (1 << base); i+=2){
		bool f = true;
		if (cnt == 50){
			break;
		}
		for (int k = 2; k <= 10; k++){
			ll t = 0;
			ll cur = 1;
			for (int j = 0; j < base; j++){
				if (i & (1 << j)){
					t += (cur);
				}
				cur *= k;
			}
			if ((del[k] = (prime(t))) == 0){
				f = false;
				break;
			}
		}
		if (f){
			cnt++;
			vector <int> v;
			for (int j = 0; j < base; j++){
				if (i & (1 << j)){
					v.push_back(1);
				}
				else{
					v.push_back(0);
				}
			}
			reverse(v.begin(), v.end());
			for (int j = 0; j < (int)v.size(); j++){
				cout << v[j];
			}
			cout << " ";
			for (int j = 2; j <= 10; j++){
				cout << del[j] << " ";
			}
			cout << "\n";
		}
	}
	return 0;
}