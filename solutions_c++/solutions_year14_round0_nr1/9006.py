#include <cstdio>
#include <iostream>
#include <map>
using namespace std;
int main() {
    int T, res1, res2, cnt, numero, dato;
    cin>>T;
    for(int caso=1 ; caso<=T ; caso++) {
    	cin>>res1;
    	map<int,bool> mapa;
    	for(int i=1; i<=4 ; i++) {
    		for(int k=1 ; k<=4 ; k++) {
    			cin>>dato;
    			if(i == res1) {
    				mapa[dato] = true;
    			}
    		}
    	}
    	cnt = 0;
    	cin>>res2;
    	for(int i=1; i<=4 ; i++) {
    		for(int k=1 ; k<=4 ; k++) {
    			cin>>dato;
    			if(i == res2) {
    				if(mapa.find(dato) != mapa.end() ) {
    					cnt++;
    					numero = dato;
    				}
    			}
    		}
    	}
    	if(cnt == 0)
    		printf("Case #%d: Volunteer cheated!\n", caso);
    	if(cnt == 1)
    		printf("Case #%d: %d\n", caso, numero);
    	if(cnt > 1)
    		printf("Case #%d: Bad magician!\n", caso);
    }    
    return 0;
}