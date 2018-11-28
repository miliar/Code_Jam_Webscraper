/**
*	
*	BY : Rajan Parmar
*/
#include <iostream>
#include <string>
#include <cmath>
#include <time.h>
#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
#include <memory.h>
using namespace std;
#pragma warning(disable:4996)
#define N 30000
#define fi first
#define se second
#define mp make_pair
#define gc getchar_unlocked
#define mod 1000000007

typedef long long int ll;
typedef pair<ll, ll > pi;
typedef pair<ll, pi > pii;


int main() {


	freopen("B-large (2).in", "r", stdin);
	freopen("B-large (2)-sol.out", "w", stdout);
	int t;
	int c;
	int n;
	string s;
	cin >> t;
	c = 1;
	int zero , one;
	
	while (t--){
		zero = one = 0;
		cin >> s;
		int i = 0;
		n = s.length();
		while(i < n){
			if(i < n && s[i] == '-'){
				zero++;
				while(i < n && s[i]=='-')
					i++;
			}
			if(i < n && s[i] == '+'){
				one++;
				while(i < n && s[i]=='+')
					i++;
			}
			
		}
		if(one == 0 || zero == 0){
			if(one == 0)
				cout << "Case #" << c++ <<": 1\n" ;
			else
				cout << "Case #" << c++ <<": 0\n" ;
		}
		else{
			if(s[0]=='-')
				cout << "Case #" << c++ <<": " << (2 * zero) - 1<<"\n";
			else
				cout << "Case #" << c++ <<": " << (2 * zero) <<"\n";
		}	
					
	}
	
	return 0;
}
