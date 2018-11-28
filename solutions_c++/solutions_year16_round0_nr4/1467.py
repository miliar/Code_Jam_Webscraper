#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long int ulli;
typedef long long int lli;
#define pb push_back
#define ft first
#define se second
#define mp make_pair

int main(){
	int t;
	cin >> t;
	for(int no = 1; no <= t; no++){
		int k, c, s;
		cin >> k >> c >> s;
		cout << "Case #" << no << ": ";
		for(int i = 1; i <= k; i++){
			cout << i;
			if(i != k) cout << " ";
		}
		cout << endl;
	}
}