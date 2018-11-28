#include <bits/stdc++.h>
#define F first
#define S second
typedef long long ll;
using namespace std;

bool compareF(const pair<int,char>& left, const pair<int,char>& right){
	return left.F > right.F;
}

bool compareS(const pair<int,char>& left, const pair<int,char>& right){
	return left.S > right.S;
}

int main(){
	ll T,n,i;
	cin >> T;
	for(int test = 1; test <= T; test++){
		cin >> n;
		pair<int,char> p[n];
		for(i = 0; i < n; i++){
			cin >> p[i].F;
			p[i].S = 'A' + i;
		}
		sort(p, p + n, compareF);
		
		cout << "Case #" << test << ": ";

		while(p[0].F>p[1].F){
			cout << p[0].S << " ";
			p[0].F--;
		}

		for(i = 2; i < n; i++){
			while(p[i].F>0){
				cout << p[i].S << " ";
				p[i].F--;
			}
		}

		while(p[0].F>0){
			cout << p[0].S << p[1].S << " ";
			p[0].F--;
		}
		cout << endl;
	}
	return 0;
}