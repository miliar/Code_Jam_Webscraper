#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

const int N = 1000;

vector <int> L;
vector <int> Div;
vector <int> Res[N];
vector <int> Coins[N];

int Pierwsza(int p){
	int i,suma,j,k,pot;
	k = 10*1000;
	for(i=2; i <= k; i++) {
		suma = 0;
		pot = 1;
		for(j=0; j<L.size(); j++){
			suma += pot*L[j];
			pot *= p;
			pot %= i;
		}
		suma %= i;
		if(suma == 0) return i;
	}
	return 1;
}

int main(){
	int i,x,j,ile,n,k;
	scanf("%d%d", &n,&k);
	ile = 0;
	for(i=0; i<(1<<(n-2)); i++){
		L.clear();
		Div.clear();
		L.push_back(1);
		for(j=0; j<n-2; j++) {
			if(1<<j & i) L.push_back( 1 );
			else L.push_back(0);
		}
		L.push_back(1);
		for(j=2; j<=10; j++){
			Div.push_back( Pierwsza(j) );
			if(Div.back() == 1) break;
		}
		if(Div.back() != 1){
			Coins[ile] = L;
			Res[ile] = Div;
			ile++;
		}
		if(ile == k) break;
	}
	printf("Case #1:\n");
	for(i=0; i<ile; i++){
		reverse(Coins[i].begin(),Coins[i].end());
		for(j=0; j<Coins[i].size(); j++) printf("%d", Coins[i][j]);
		printf(" ");
		for(j=0; j<Res[i].size(); j++) printf("%d ", Res[i][j]);
		printf("\n");
	}
	return 0;
}
