#include<iostream>
#include<cstdio>
#include<string>
#include <stdio.h>
using namespace std;
int T, t1[4][4],t2[4][4], r1, r2, x, z;
int main()
{ 
	scanf("%d", &T);
	FILE *plik = fopen("wynik.txt", "w");
	for (int i =0; i<T; i++){
		x =0;
		cin>>r1;
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++){
				cin>>t1[j][k];
			}
		}
		
		cin>>r2;
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++){
				cin>>t2[j][k];
			}
		}
		
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				if(t1[r1-1][i] == t2[r2-1][j]){
					x++;
					z = t1[r1-1][i];
				}			
			}
		}
		if(x ==0){
//			cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
			fprintf(plik, "Case #%d: Volunteer cheated!\n", i+1);
		}
		else if(x ==1){
//			cout<<"Case #"<<i+1<<": "<<z<<endl;
			fprintf(plik, "Case #%d: %d\n", i+1, z);
		}
		else{
//			cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
			fprintf(plik, "Case #%d: Bad magician!\n", i+1);
		}
		
	}
    cin.ignore();
    getchar();
    return 0;
    
}

