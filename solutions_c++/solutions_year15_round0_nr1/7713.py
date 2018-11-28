#include<bits/stdc++.h>
using namespace std ;

int main() {
	ifstream cin("input.txt") ;
	ofstream cout("output.txt") ;
	int t ;
	cin >> t ;
	for(int test=1;test<=t;test++) {
		int k ;
		cin >> k ;
		string str ;
		cin >> str ;
		
		int till = 0 , ans = 0 ;
		till = str[0]-'0' ;
		for(int i=1;i<=k;i++) {
			int temp = str[i]-'0' ;
			if(i > till) {
				ans += (i-till) ;
				till += (i-till) + temp ;
			}
			else {
				till += temp ;
			}
		}
		cout << "Case #" << test << ": " ;
		cout << ans << endl;
	}
}
