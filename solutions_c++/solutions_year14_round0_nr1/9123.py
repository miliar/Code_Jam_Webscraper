#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <fstream>

using namespace std;
//#define SMALL
#define LARGE

int main(){
    
#ifdef LARGE    
    freopen("A-small-attempt1.in", "rt", stdin);
    freopen("A-small-attempt1.out", "wt", stdout);
#endif    
	int T,R,ind;
    int mat[4][4];
    int test[8];
    cin >> T;
    for(int cur = 1; cur<= T; cur++){
		int i=0,k=0,t=4;
		while(i<2){
			cin >> R;
			for(int j=0;j<4;j++){
				for(int h=0;h<4;h++){
					cin>>mat[j][h];
					}
				}
			int f=0;
			while(k<t){
				test[k]=mat[R-1][f];
				k++;
				f++;
			}
			t=8;
		i++;
		}
		int compt=0;
		for(int i=0;i<8;i++){
			for(int j=i+1;j<=8;j++){
				if(test[i]==test[j]){
					compt++;
					ind=i;
					}
				}
			}
		if(compt==1){
			printf("Case #%d: %d\n", cur,test[ind]);}
		else if(compt>1){
			printf("Case #%d: Bad magician!\n",cur);}
		else {
			printf("Case #%d: Volunteer cheated!\n",cur);}
    }
	
    return 0;
}

