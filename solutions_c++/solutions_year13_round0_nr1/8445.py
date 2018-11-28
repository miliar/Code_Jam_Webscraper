#include "stdafx.h"
#include "string.h"
#include <stdio.h>


#define FOR(k,N) for(k=0; k<N; k++)
#define FOR_1(k,N) for(k=1; k<=N; k++)

#define  MAX 4
#define X_WON 0
#define O_WON 1
#define DRAW 2
#define NC 3

#define win_O 0
#define win_X 1

//int  array[MAX][MAX];
char  array[MAX][MAX];

int main(void)
{
	FILE *fr,*fw;
    int i,j,k,T;
    char status=NC;
    char diag1,diag2, row_c,col_c;
	char row=1,col=1,diag_L=1,diag_R=1,dot=0;

    memset(array,0,sizeof(char)*MAX*MAX);

	fr=fopen("input.txt","r");
	if(fr==NULL)
	{
		printf("File read error!\n");
		return 0;
	}
	fw=fopen("output.txt","w");
	if(fw==NULL)
	{
		printf("File write error!\n");
		return 0;
	}
	///////////////////////////////////////////

	fscanf(fr,"%d",&T);
    fgetc(fr); // skip next line

	FOR_1(k,T)
	{
		//RESET	
        status=NC;
        diag_R=1;
        diag_L=1;
        dot=0;
        
        //scan the array

        FOR(i,MAX)
        {
            FOR(j,MAX)
            {
                //fscanf(fr,"%d",array+i*MAX+j) ;
                fscanf(fr,"%c",&array[ i ][ j ]) ;
            }
            fgetc(fr); // skip next line
        }
        //fgetc(fr); // skip next line
        //fgetc(fr); // skip next line


        diag1=array[0][0];
        diag2=array[0][3];

        // Algorithm starts
        FOR(i,MAX)
        {
            row=1;
            col=1;

            if(diag_L && diag1 != array[ i ][ i ] && array[ i ][ i ] != 'T' && diag1 !='T')
            {
                diag_L =0;
            }
           if(diag_R && diag2 != array[ i ] [ MAX-1-i ]   && array[ i ] [ MAX-1-i ]  !='T' && diag2 !='T')
            {
                diag_R =0;
            }
           //get value from next 
           if(array[ i ][ i ] != 'T')
                diag1=array[ i ][ i ] ; // diagonal left

           if(array[ i ] [ MAX-1-i ]  !='T')
                diag2= array[i] [ MAX-1-i ] ; //right

            FOR(j,MAX)
            {
                row_c=array[ i ][ j ];
                col_c=array[ j ][ i ];

                if(diag1!=row_c && row_c !='T')
                {
                    row=0;
                }
                if(diag1!=col_c && col_c !='T')
                {
                    col=0;
                }
                if( dot==0 && row_c == '.')
                    dot=1;
                /*if(row ==0 && col==0)
                    break;*/
            }
            if(row || col)
            {
                if(diag1=='X')
                    status=X_WON;

                if(diag1=='O')
                    status=O_WON;
                break;
            }
        }
        if( !(status == X_WON || status==O_WON))
        {
            if(diag_L)
            {
                    if(diag1=='X')
                        status=X_WON;

                    if(diag1=='O')
                        status=O_WON;
            }
            else if(diag_R)
            {
                if(diag2=='T')
                {
                    if(array[0][3]=='X')
                        status=X_WON;

                    if(array[0][3]=='O')
                        status=O_WON;
                }
                else
                {
                    if(diag2=='X')
                        status=X_WON;

                    if(diag2=='O')
                        status=O_WON;                
                }
            }

            if(dot==0 && !(status == X_WON || status==O_WON) )
                status=DRAW;
            //else
             //   status=NC;
        }
		//Algo Ends
        fprintf(fw,"Case #%d: ",k);
        switch(status)
        {
            case X_WON:
    	        fprintf(fw,"X won\n");
                break;
            case O_WON:
    	        fprintf(fw,"O won\n");
                break;
           case DRAW:
    	        fprintf(fw,"Draw\n");
                break;
            case NC:
    	        fprintf(fw,"Game has not completed\n");
                break;
            default:
    	        fprintf(fw,"Wrong!\n");
        }

        fgetc(fr);
	
	}

	return 0;
}

