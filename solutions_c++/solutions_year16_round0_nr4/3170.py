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

int n,k;

int main(){
	
	freopen("4.in", "r", stdin);
	freopen("4.out", "w", stdout);
	
	int t=0;
	cin >> t;
	
	for( int i=1;i<=t;i++){
		long long a,b,c;
		scanf("%lld%lld%lld",&a,&b,&c);
		printf("Case #%d: ",i);
		for( int j=1;j<c;j++)
			cout << j << " ";
		long long power = 1;
		
		for( int j=1;j<=b;j++)
			power *= a;
		cout << power << endl;
	}
	return 0;
}
