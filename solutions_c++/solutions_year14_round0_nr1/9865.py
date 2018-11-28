#include <iostream>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
#define CHEAT_MAGICIAN -1
#define CHEAT_VOLUNTEER 0

void runCase ( int caseNumber );
int main(int argc, char** argv) {
    freopen("input.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);

	//...Setup variables
	int tCase = -1;

	//...get test cases
	scanf ( "%d" , &tCase );	
	
	//...test cases
	for ( int cCase=1; cCase<=tCase; cCase++ ){
		runCase ( cCase );
	}
	
	///....exit	
	return 0;
}

void runCase ( int caseNumber ) {
		//...Set up deck
		int answer = -1,input=-1,match=0;
		int d[4][4];
		int m[2][4];
		
		//...Two cycles
		for ( int x=0;x<=1;x++){
			
			//...Get Volunteers answer
			scanf ( "%d" , &answer);			
			for ( int line=0;line<4;line++) {
				
				//...get a line	of the deck
				scanf("%d %d %d %d" , &d[line][0] , &d[line][1] , &d[line][2] , &d[line][3] );   
			}			

			//...map line answer
			for ( int i=0;i<4;i++){
				m[x][i] = d[answer-1][i];
			}
		}	

		//...Match two numbers | O(NM)
		for ( int i=0;i<4;i++){
			for ( int ii=0;ii<4;ii++){
				if ( m[0][i] == m[1][ii] ){
					match++;
					answer = m[1][ii];
				}	
			}			
		}	

		
		if (match>1)match=CHEAT_MAGICIAN;
				
		//...Output result
		switch ( match ) {
			case CHEAT_MAGICIAN: 	printf ("Case #%d: Bad magician!\n" 		, caseNumber );	break;		
			case CHEAT_VOLUNTEER:	printf ("Case #%d: Volunteer cheated!\n" , caseNumber);	break;
			default:				printf ("Case #%d: %d\n" 				, caseNumber, answer);
		}
}

