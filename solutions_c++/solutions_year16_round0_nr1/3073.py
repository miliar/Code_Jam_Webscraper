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

int check[11];

int fill(){
	for(int i = 0 ; i < 10 ; i++){
		if(check[i]==0)
			return 1;
	}
	return 0;
}
int main() {


	freopen("A-large.in", "r", stdin);
	freopen("A-large-sol.out", "w", stdout);
	int t;
	int c;
	ll n;
	cin >> t;
	c = 1;
	while (t--){
		memset(check , 0 , sizeof(check));
		cin >> n;
		if(n==0)
			cout << "Case #" << c++ <<": INSOMNIA\n" ;
		else{
			int mul = 0;
			while(fill()){
				mul ++ ;
				ll tmp = n*mul;
				while(tmp!=0){
					check[tmp%10] = 1;
					tmp/=10;					
				}
				
			}
			cout << "Case #" << c++ <<": " << n * mul << "\n";
		}
			
	}
	
	return 0;
}
