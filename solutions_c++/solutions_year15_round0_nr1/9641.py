#include <iostream>
#include <bits/stdc++.h>
using namespace std;
#define ll long long
string shy;
 
int main() {
 
	ll t , n , i , j , k , smax;
	cin >> t ;
	ll cnt = 0;
	ll add = 0;
	for( j = 1 ; j <= t ; j++){
		cin >> smax ;
		cnt = 0 ; 
		add = 0;
		cin >> shy;
		for(i = 0 ; i <= smax ; i++){
			k = int(shy[i])-'0';
			if(i==0){
				cnt+=k;
 
 
			}
			else{
 
				if(i<=cnt){
 
					cnt+=k;
 
				}
				else{
					add+=i-cnt;
 
					cnt+=i-cnt+k;
				}
			}
 
 
		}
		cout << "Case #"<<j<<": "<<add << endl ;
 
	}
	return 0;
}