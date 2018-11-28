//#include "stdafx.h"
#include <iostream>
#include "stdio.h"


//using namespace std;

#define NUMBER_CARDS 16
#define ARRAY_SIZE 4 

int main()

{
	int T;
        int CaseNo = 1;
	int sampleA [4][4] = {};
	int sampleB [4][4] = {};
	int h,i,j,k;
	int first_A = 0;
	int second_A = 0;
	int RowA [4] = {};
	int RowB [4] = {};

	enum result_type {RESET,NONE,MATCH,CHEAT,BAD};
	result_type result = RESET;
	int answer = 0;

	freopen ("output.txt","w",stdout);
	freopen ("input.txt","r",stdin);

	//Get the no of testcases
	scanf("%d",&T);


    while (T--){






        result = RESET ;
	//Get the first answer what row A

	scanf("%d",&first_A);
	// scan the card sequence A
	for (i=0; i< ARRAY_SIZE;i++ ){

		for (j=0;j< ARRAY_SIZE;j++)
		{
			scanf("%d", &sampleA[i][j]);
			//printf(" %d ...\n",  sampleA[i][j]); //SB
		}
	}
	//Get the answer row B 
	scanf("%d",&second_A);
	// scan the card sequence B

	for (i=0; i< ARRAY_SIZE;i++ ){

		for (j=0;j< ARRAY_SIZE;j++)
		{
			scanf("%d", &sampleB[i][j]);
		}
	}

	// Process
	for (i=0; i< ARRAY_SIZE ; i++){
		RowA[i] = sampleA[first_A -1][i] ;

	}

	for (i=0; i< ARRAY_SIZE ; i++){
		RowB[i] = sampleB[second_A -1][i] ;

	}



	// Check for duplicates.

	answer = RESET;


	for (i=0; i< ARRAY_SIZE ; i++){

		for (j=0;j< ARRAY_SIZE ; j++){


			if (RowA[i] == RowB[j]){

				if (result != MATCH &&  result != BAD ){ 
					result = MATCH ;
					answer = RowA[i];

				}else if (result == MATCH){
					result = BAD ;  //more than 1 match. 

				}
			}


		}

	}
	// if we get here and there are no matches then we have a cheat.
	if (result == RESET){
		result = CHEAT;
	}
	//print the result. 
        printf("Case #%d: ",CaseNo++);
	switch (result)   {


		 case CHEAT :
			 printf("Volunteer cheated!\n");
			 break;

		 case BAD :
			 printf("Bad magician!\n");
			 break;

		 case MATCH :
			 printf("%d\n",answer);
			 break;

		 default :
			 printf("Error no match");



	}


    } //endwhile


} 
