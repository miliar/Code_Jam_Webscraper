#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

char change(char c)
{
	if(c == '+') return '-';
	return '+';
}
int main(){
	int t; string cad;
	scanf("%d",&t);
	int caso = 1;
	while(t--){
		cin >> cad;
		int plus  = 0;
		int minus = 0;
		for(int i = 0;i < cad.size();i++){
			if(cad[i] == '+') plus++;
			else minus++;
		}
		if(plus == cad.size()) printf("Case #%d: 0\n",caso++);
		else if(minus == cad.size()) printf("Case #%d: 1\n",caso++);
		else{
			cad = cad;
			char init = cad[0];
			int pos = 0;
			int flip = 0;
			while(pos < cad.size()){
				if(cad[pos] == init) pos++;
				else{
					flip++;
					if(init == '+'){
						plus -= pos;
						minus += pos;
					}
					else{
						plus += pos;
						minus -= pos;
					}					
					init = change(init);
				}
				if(plus == cad.size()) break;
				if(minus == cad.size()){
					flip++;
					break;
				}
			}
			printf("Case #%d: %d\n",caso++,flip);
		}
	}
	return 0;
}
