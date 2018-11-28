#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	int t,s; int caso = 1;
	string cad; int acum;
	scanf("%d",&t);
	while(t--){
		cin >> s >> cad;
		int acum = 0;
		int res = 0;
		for(int i = 0;i < cad.size();i++){
			if(acum >= i){
				acum += (int)(cad[i] - '0');
			}
			else{
				res += (i - acum);
				acum += (i - acum) + (int)(cad[i] - '0');
			}
		}
		printf("Case #%d: %d\n",caso,res);
		caso++;
	}
	return 0;
}
