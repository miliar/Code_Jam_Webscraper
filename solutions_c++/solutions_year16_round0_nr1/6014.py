#include <bits/stdc++.h>
#define optimizar_io ios_base::sync_with_stdio(0);cin.tie
using namespace std;

bool ap[12];

int N;
int K;
int act,aux;
bool malos;

int main(){
	optimizar_io(0);
	cin>>N;
	for(int i = 1; i <= N; i++){
		cin>>K;
		if(K!=0){
			act = 0;
			for(int j =0 ;j < 10; j++)
				ap[j] = false;
			while(true){
				act += K;
				aux = act;
				while(aux){
					ap[aux%10] = true;
					aux/=10;
				}
				malos = false;
				for(int j=0;j < 10;j++)
					if(!ap[j]){
						malos = true;
						break;
					}
				if(!malos){
					cout<<"Case #"<<i<<": "<<act<<"\n";
					break;
				}
			}
		} else {
			cout<<"Case #"<<i<<": INSOMNIA\n";
		}
	}
	return 0;
}