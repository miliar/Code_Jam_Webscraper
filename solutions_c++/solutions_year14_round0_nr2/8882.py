#include<iostream>
#include<cstdio>
#include<string>
#include <stdio.h>
using namespace std;
double c, f, x, cnf, inm, nextinm, czas, cps, nextcps;
int z, T;
int main()
{ 
	scanf("%d", &T);
	FILE *plik = fopen("wynikB.txt", "w");
	for (int i =0; i<T; i++){
		z=0;
		cin>>c>>f>>x;
		int d = x/f, j=0;
//		double t[d+1], ciastka[2][d+1];
		cps = 2;
		czas = 0;
		j=0;
//		ciastka[0][j] = cps;
		while(z == 0){
			cnf = c/cps;
			inm = x/cps;
//			t[j]=inm+czas;
//			j++;
			nextcps = cps+f;
			nextinm = x/nextcps;
			if( cnf + nextinm < inm ){
				cps = nextcps;
//				ciastka[0][j] = cps;
				czas+= cnf;
			}
			else{
				czas+=inm;
				z = 1;
			}
//			for(int i=0; i<j; i++){
				
//				ciastka[1][i] = ciastka[0][i]*czas;
/*				if(ciastka[1][i]>x){
					fprintf(plik, "!! %f %f\n",ciastka[0][i], ciastka[1][i]);
				}
*/				//cout<<"!!!"<<endl;
//			}
//			cout<<"czassss  "<<czas<<endl;
		}
//		cout<<"teraz ";
//		for(int i =0; i<j; i++){
//			cout<<t[i]<<" ";
//			if(t[i]<czas){
//				czas = t[i];
//			}
//		}
//		cout<<endl;
			printf("Case #%d: %.07f\n", i+1, czas);
			fprintf(plik, "Case #%d: %.07f\n", i+1, czas);
	}
    cin.ignore();
    getchar();
    return 0;
    
}
