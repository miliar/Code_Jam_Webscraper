#include <iostream>
#include <fstream>
#include <sstream>
#include <ctime>
#include <cmath>
#include <vector>
#include <queue>
#include <string.h>
#include <time.h>
//#include <unistd.h>
using namespace std;


char line[10000];
	


void swap(int& R,int& C) {
	if (C>R) {
		int temp=C;
		C=R;
		R=temp;
	}
}
	
int main(int argc,char*argv[]) {
	int T;
	scanf("%d\n",&T);
	
	
	int X,R,C;
	char win;
	
	for (int iter=1;iter<=T;iter++) 
	{
		scanf("%d %d %d\n",&X,&R,&C);
		swap(R,C);
		
		win=' ';
		
		
		// 1. quick check
		if ((R*C)%X>0)
			win='R';
		else {

			if (X==1||X==2) {
				win='G';
			}
			
			if (X==3) {			
				if (R==1||C==1) // bad
					win='R';
				else if (R==2&&C==2) // bad
					win='R';
				else  //  at least 2*3 --> ok
					win='G';
			}
			
			if (X==4) {
				if (R>=4&&C>=4)  // ok
					win='G';
				else if (R<4&&C<4) // bad
					win='R';
				else if (R<=2||C<=2) // bad
					win='R';
				else   // 3* factor_of_4  --> ok
					win='G';
			}
		}
			
		// 2. exist some domino to make incessible hole < X
		
		printf("Case #%d: ",iter);
		if (win=='R')
			printf("RICHARD\n");
		else if (win=='G')
			printf("GABRIEL\n");
		else 
			printf("%c\n",win);
	}
	
	return 0;

}