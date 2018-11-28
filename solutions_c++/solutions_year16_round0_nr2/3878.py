#include <bits/stdc++.h>

#define db 	cout << "*****" << endl;
#define Max 100009
#define pb push_back
#define pp pop_back
#define ff first
#define ss second
#define mk make_pair
#define MOD 1000000007

using namespace std;

map < string , bool > mapp;

queue < pair < string , int > > Q;
 
int main(){
	
	
	freopen("2.in" , "r" , stdin);
	freopen("2.out" , "w" , stdout);
	
	int t=0;
	
	cin >> t;
	for( int i=1;i<=t;i++){
		
		string s;
		cin >> s;
		
		int n = s.size();
		int ans=1;
		char last = s[0];
		for( int j=1;j<n;j++){
			if( s[j] != last ){
				ans++;
				last = s[j];	
			}
		}
		if( last == '+' )
			ans--;
		
		printf("Case #%d: %d\n",i , ans);
		
	}
	return 0;
}
