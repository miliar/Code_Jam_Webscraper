#include <iostream>
#include <cstdio>
using namespace std;

int v[20];
int n;
int prim, sec;
int conta;
int card;
int row;
int elem;

void process(){
	conta = 0;
	for(int i = 1; i<=16; i++){
		if(v[i] == 2) {conta++;elem = i;}
	}
}

void read_input(){
		//read input
		scanf("%d",&row);
			for(int i = 1; i<=4; i++){
				for(int j = 1; j<=4; j++){
					scanf("%d",&card);
					if(i == row){
						v[card]++;
					}	

				}
			}

}

int main(){
	int c_local = 1;
	scanf("%d",&n);
	while(n--){

		//clean v[]
		for(int i=1;i<=16;i++) v[i] = 0;

		read_input();
		read_input();

		process();

		//print output
		printf("Case #%d: ", c_local++);
		if(conta == 1){
			printf("%d", elem);
		} else if(conta>1){

			printf("Bad magician!");
		
		} else  
			printf("Volunteer cheated!");

		printf("\n");

	}

	return 0;
}
