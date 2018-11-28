#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>

using namespace std;
typedef vector<int> VI;

int main(){
	int N, t;
	cin >> N;
	for(int i=0;i<N;++i){
		cin >> t;
		if(t==0){
			printf("Case #%d: INSOMNIA\n", t+1);
			continue;
		}
		VI mapa(10,0);
		int cont=0;
		int x;
		for(int m=1; cont<10;++m){
			x = t*m;
			int cx=x;
			while(cx){
				int d=cx%10;
				if(!mapa[d]){
					mapa[d]=1;
					cont++;
				}
				cx/=10;
			}
		}
		printf("Case #%d: %d\n", i+1, x);
	}
}
