#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
using namespace std;

int cartas1[6][6];
int cartas2[6][6];

int main() {
	int T ,c1,c2;
	int rpta;
	scanf("%d",&T);
	for (int i=1;i<=T;i++){
		int cont=0;
		scanf("%d",&c1);
		for (int j=1;j<=4;j++)
			for (int k=1;k<=4;k++)
				cin>> cartas1[j][k] ;
		scanf("%d",&c2);
		for (int j=1;j<=4;j++)
			for (int k=1;k<=4;k++)
				cin>> cartas2[j][k]	;
		
		for (int j=1;j<=4;j++){
			for (int k=1;k<=4;k++){
				if(cartas1[c1][j]==cartas2[c2][k]) {
					rpta=j;cont++;
				}
			}
		}
		 if(cont>1)	 cout << "Case #" <<  i <<": " << "Bad magician!"  << endl;
	else if(cont==0) cout << "Case #" <<  i <<": " << "Volunteer cheated!"  << endl;  
	else 			 cout << "Case #" <<  i <<": " << cartas1[c1][rpta]  << endl;
	}
	return 0;
}