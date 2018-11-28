#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
bool check[10] ;
typedef long long ll ;
void fen(ll tmp , int &Enum){
	while(tmp){
			int num = tmp%10 ;
			if(!check[num]) {
				check[num] = true ;
				Enum++ ;
			}
			tmp/=10;
	}
	return ;	
}
using namespace std;
int main(){
	//freopen("in.txt","r",stdin) ;
	//freopen("out.txt","w",stdout);
	int t,cas = 1 ;
	ll n ;
	cin >> t ;
	while(t--){
		memset(check,0,sizeof(check)) ;
		//system("pause") ;
		cin >> n ;
		//n = t ;
		printf("Case #%d: ",cas++) ;
		if(!n) {
			cout << "INSOMNIA" << endl;
			continue; 	
		}
		int Enum = 0;
		ll tmp = n;
		fen(n,Enum) ;
		while(Enum<10){
			n+=tmp;
			//cout << n << endl;
			fen(n,Enum) ;
		}
		cout << n << endl; 	
	}
	//fclose(stdin) ;
	//fclose(stdout) ;
	return 0;
} 
