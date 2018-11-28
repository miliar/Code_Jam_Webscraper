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

bool isp( long long a){
	
	for( long long i=2;i<=sqrt(a);i++)
		if( a % i == 0 )
			return 0;
			
	return 1;	
}
int jog[12];
long long arr[12];

void fun( int ind){
	
	if( k<= 0 ) return;
	
	if( ind == n ){
		
		jog[ind]=1;
		
		for( int i=2;i<=10;i++){
			long long pow=1;
			arr[i]=0;
			
			for( int j=ind;j>=1;j--){
				arr[i] += jog[j] * pow;
				pow*=i;	
			}	
			
		}
		for( int i=2;i<=10;i++){
			if( isp( arr[i]) == 1  )
				return;
		}	
		
		k--;
		jog[ind]=1;
		
		for( int i=1;i<=ind;i++) cout << jog[i];
			cout << " ";
		for( int i=2;i<=10;i++){
			for( int j=2;j<=arr[i];j++){
				if( arr[i] % j == 0 ){
					cout << j << " ";
					break;	
				} 
			}	
		}
		cout << endl;
		
		return;
			
	}	
	
	if( ind != 1 )
		fun( ind + 1);
		
	jog[ind] = 1;
	fun( ind + 1);
	jog[ind] = 0 ;
	
	return;
}
int main(){
	
	
	int t=0;
	freopen("3.in" , "r" , stdin);
	freopen("3.out" , "w" , stdout);
	
	cin >> t;
	cin >> n >> k;
	
	cout << "Case #1:\n";
	fun(1);
	
	return 0;
}
