#include <bits/stdc++.h>

#define debug(x) cout << #x << " = (" << x << ")\n"

typedef unsigned long long int ull;
typedef long long ll;

using namespace std;
bool num[10];
int cont;

ull decomp(int Ori, int i){
	int aux ;
	ull N = Ori * i;
	while( N ){
		aux = N % 10;
		if(!num[aux]){
			num[aux] = 1;
			cont++;
		}	
		N = (N - aux)/10;
	}
	
	if( cont == 10 )
		return Ori*i;
	else
		decomp(Ori, i+1);
}

int main(){

	int T, N;
	ull ans;
	
	cin >> T ;
	
	for ( int i = 0 ; i < T ; i++ ){
	
		ans = cont = 0;
		for( int j = 0 ; j < 10 ; j++ ){
			num[j] = 0;
		}

		cin >> N;

		if(N != 0){
			
			ans = decomp( N , 1 ) ;
			cout << "Case #" << i+1 << ": " << ans << endl;
		}else
			cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;	
	}

}
