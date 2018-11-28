#include <iostream>
#include <algorithm>
#include <cstdio>

using namespace std;


int main(){

	int t;
	cin>>t;
	int c = 1;
	while(t--){
		printf("Case #%d: ", c++);
		int a;
		cin>>a;
		a--;
		int v1[4];
		for(int i = 0;i<4;i++){
			for(int j = 0;j<4;j++){
				int x;
				cin>>x;
				if(i == a)v1[j] = x;
			}
		}
		int v2[4];
		cin>>a;
		a--;
		for(int i = 0;i<4;i++){
			for(int j = 0;j<4;j++){
				int x;
				cin>>x;
				if(i == a)v2[j] = x;
			}
		}

		int qtd = 0;int resp = -1;
		for(int i = 0;i<4;i++){
			for(int j = 0;j<4;j++){
				if(v1[i] == v2[j]){
					qtd++;
					resp = v1[i];
				}
			}
		}

		if(qtd == 0)
			printf("Volunteer cheated!\n");
		else
		if(qtd!=1)
			printf("Bad magician!\n");
		else
			printf("%d\n",resp);

	}
	return 0;
}