#include <bits/stdc++.h>
#define optimizar_io ios_base::sync_with_stdio(0);cin.tie
using namespace std;
typedef long long int lli;

lli pots[12][18];
vector<int> lista;

int N;
int T,J;
int cont;
lli aux;
int buenos;
bool noPrimo;


int main(){
	optimizar_io(0);
	cin>>T>>N>>J;
	if(N==16&&J==50){
		cout<<"Case #1:\n";
		for(int i =2 ; i <= 10; i++){
			pots[i][0] = 1;
			for(int j = 1; j < 16; j++){
				pots[i][j] = pots[i][j-1]*i;
			}
		}
		for(int i = 0; i < (1<<16);i++){
			if(cont == 50)
				break;		
			if((i&1)&&(i>>15)&1){
				buenos = 0;
				for(int j =2 ; j <= 10;j++){
					aux = 0;
					for(int k = 0; k < 16; k++)
						if(i&(1<<k))
							aux += pots[j][k];
					noPrimo = false;
					for(lli k = 2; k*k <= aux;k++){
						if(aux%k==0){
							noPrimo = true;
							lista.push_back(k);
							break;
						}
					}
					if(!noPrimo){
						lista = vector<int>();
						break;
					} else {
						buenos++;
					}
				}
				if(buenos == 9){
					for(int j = 15; j >= 0 ; j --){
						if(i&(1<<j))
							cout<<1;
						else
							cout<<0;
					}				
					for(int i = 0; i < lista.size();i++)
						cout<<" "<<lista[i];
					cout<<"\n";
					cont++;
					lista = vector<int>();
				}
			}
		}
	}
	return 0;
}