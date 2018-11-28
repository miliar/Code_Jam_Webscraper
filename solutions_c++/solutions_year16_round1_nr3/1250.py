#include <bits/stdc++.h>

#define db 	cout << "*****" << endl;
#define Max 109
#define pb push_back
#define pp pop_back
#define ff first
#define ss second
#define mk make_pair
#define MOD 1000000007

using namespace std;

int n,k;
int A[Max];
int ans=1;
int arr[Max];
bool vis[Max];

void chk(  int nw ){
	
	arr[nw+1] = arr[1];
	arr[0] = arr[nw];
	
	for( int i=1;i<=nw;i++)
		if( A[arr[i]] != arr[i-1] && A[arr[i]] != arr[i+1]  )
			return;
	ans = nw ;
}
int fun( int nw){
	
	if( nw-1 > ans )
		chk( nw-1 );	
	
	if( nw == n + 1 )
		return 0;
	
		
	for( int i=1;i<=n;i++){
		if( vis[i] == 0 ){
			
			arr[nw] = i;
			
			vis[i] = 1 ;
			fun( nw + 1 );
			vis[i] = 0 ;	
			
			
		}
	}
	return 0;
}
int main(){
	
	
	int T=0;
	
	freopen("3.in" , "r" , stdin);
	freopen("three.out" , "w" , stdout);
	
	cin >> T;
	for( int t=1;t<=T;t++){
		
		cin >> n;	
		for( int i=1;i<=n;i++)
			cin >> A[i];
		
		ans = 0;
		fun( 1 );
		
		cout << "Case #" << t << ": ";
		cout << ans << endl;
		
	}
	return 0;
}
