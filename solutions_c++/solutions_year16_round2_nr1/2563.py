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

int ar[100] ; 

int main() {


	freopen("A-large.in", "r", stdin);
	freopen("A-large-sol.out", "w", stdout);
	
	int c;
	int t;
	string s;
	cin >> t;
	c = 1;
	while(t--){
		vector <int> vec;
		cin >> s;
		memset(ar , 0 , sizeof(ar));
		
		for(int i = 0 ; i < s.length() ; i++){
			ar[s[i]]++;
		}
		while(ar['Z']>0 && ar['E']>0 && ar['R']>0 && ar['O']>0 ){
			ar['Z']--;
			ar['E']--;
			ar['R']--;
			ar['O']--;
			vec.push_back(0);
		}
		while(ar['S']>0 && ar['I']>0 && ar['X']>0  ){
			ar['S']--;
			ar['I']--;
			ar['X']--;
			
			vec.push_back(6);
		}
		
		while(ar['S']>0 && ar['V']>0 && ar['E']>1 && ar['N']>0){
			ar['S']--;
			ar['V']--;
			ar['N']--;
			ar['E']-=2;
			
			
			vec.push_back(7);
		}
		
		while(ar['E']>0 && ar['I']>0 && ar['G']>0 && ar['H']>0 && ar['T']>0 ){
			ar['T']--;
			ar['H']--;
			ar['G']--;
			ar['I']--;
			ar['E']--;
			
			vec.push_back(8);
		}
		
		while(ar['F']>0 && ar['U']>0 && ar['R']>0 && ar['O']>0 ){
			ar['F']--;
			ar['U']--;
			ar['R']--;
			ar['O']--;
			vec.push_back(4);
		}
		
		while(ar['T']>0 && ar['W']>0 && ar['O']>0  ){
			ar['O']--;
			ar['T']--;
			ar['W']--;
			
			vec.push_back(2);
		}
		while(ar['F']>0 && ar['I']>0 && ar['V']>0 && ar['E']>0 ){
			ar['F']--;
			ar['I']--;
			ar['V']--;
			ar['E']--;
			vec.push_back(5);
		}
		
		while(ar['T']>0 && ar['H']>0 && ar['E']>1 && ar['R']>0 ){
			ar['T']--;
			ar['H']--;
			ar['R']--;
			ar['E']-=2;
			
			vec.push_back(3);
		}
		
		
		
		
		
		
		
		
		while(ar['N']>1 && ar['I']>0  && ar['E']>0 ){
			ar['N']-=2;
			ar['I']--;
			
			ar['E']--;
			vec.push_back(9);
		}
		while(ar['O']>0 && ar['N']>0 && ar['E']>0  ){
			ar['O']--;
			ar['N']--;
			ar['E']--;
			
			vec.push_back(1);
		}
		
		sort(vec.begin() , vec.end());
		cout << "Case #" << c++ <<": " ;
		for(int i = 0 ; i < vec.size() ; i++){
			cout << vec[i];
		}
		cout << endl;
		vec.clear();
	}
		//	cout << "Case #" << c++ <<": " << "\n";
	
	
	return 0;
}
