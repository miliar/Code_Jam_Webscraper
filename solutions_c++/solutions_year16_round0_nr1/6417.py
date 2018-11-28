#include <stdio.h>
#include <stdlib.h>
#include <string.h> 
#include <iostream>
using namespace std;

int numberscontained(int alldigits[10],int num){
	int remain;
	int digitsfilled=0;
	for (int i=0;i<10;i++)
		digitsfilled+=alldigits[i];

	while(num>0 && digitsfilled<10){
		remain=num%10;
		if (alldigits[remain]==0){
			alldigits[remain]=1;
			digitsfilled++;
		}
		num=num/10;
	}
	if (digitsfilled==10)
		return 1;
	else return 0;
}



int main(){
	int T, currn; //test cases, currentn
	cin >> T;
	//T=1;
	//int * alldigits=calloc(sizeof(int),10); // 0 1 2 3 4 5 6 7 8 9 0
	int alldigits[10]={0};

	/* //test
	numberscontained(alldigits,21358);
	for (int i=0; i<10;i++){
		printf("%d: %d\n",i, alldigits[i] );
		
	}
	*/

	int allthere,iters,multipleofn; //all digits there,      value of i, as in i*n
	for (int i=0;i<T;i++){
		cin >> currn;
		//currn=1;

		allthere=0;
		iters=0;
		
		if (currn==0) {
			printf("Case #%d: INSOMNIA\n",i+1 );
		}

		else{
			while (allthere==0 ){
				iters++;
				multipleofn=iters*currn;
				allthere=numberscontained(alldigits,multipleofn);
			}

			printf("Case #%d: %d\n",i+1,iters*currn );
			memset(alldigits,0,sizeof(int)*10);
		}
	}


	
	return 0;
}