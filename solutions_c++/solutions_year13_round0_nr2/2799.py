#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <math.h>

void printMatrix();
void fillMatrix();

unsigned int v1[10][10] = {0,};
unsigned int v2[10][10] = {100,}; 

unsigned int ROW = 0;
unsigned int COL = 0;

int main()
{

// get the number of test cases
unsigned int testcase = 0;

static const char filename[] = "B-small-attempt0.in";
//static const char filename[] = "A-large.in";
//A-large-practice.in
//static const char filename[] = "A-large-practice.in";

FILE *file = fopen ( filename, "rt" );

static const char filename1[] = "Out.txt";
FILE *file1 = fopen ( filename1, "wt" );

//static const char filename2[] = "In1.txt";
//FILE *file2 = fopen ( filename2, "wt" );

//static const char filename3[] = "In2.txt";
//FILE *file3 = fopen ( filename3, "wt" );


unsigned int counter =0;
printf("karthikeyan: file=%x\n", file);
// get the number of elements
unsigned int n=0;

char line[300];
char out[100];
unsigned int i=0 , j=0, k=0, row=0,col=0, mow=1;

int result = 0;
//             scanf("%d", &j);             
             

if (file)
{
             // test case
             fgets(line, 10, file);
          	 sscanf (line, "%u", &testcase);
             printf("karthikeyan: size of testcase =%d\n", testcase);
             //scanf("%d", &j);             
             memset(line, '0', 10);
             
             for(counter=1; counter<=testcase; counter++)
             {
                  result = 1;
                  memset(line, '0', 300);                        
                  fgets(line, 300, file);
    	     	  sscanf(line,"%u %u",&row,&col);
                  //scanf("%d", &j);             
   				  printf("karhtikeyan: row=%u col=%u\n",row,col);
   				  ROW = row;
   				  COL =col;
				  //scanf("%d", &j);
				  fillMatrix();
				  // get the matrix
                  char *ptr = line;
                  int j=0;
                  for(i=0; i<row; i++)
                  {
                     j = 0;
                     memset(line, '0', 300);        
                     fgets(line, 50, file);
                     for(k=0; k<col; k++)
                     {
                        ptr = line+j;
        	            sscanf (ptr, "%u", &v1[i][k]);
                        //printf("element=%u, pos=%d\n", v1[i][k], i);
                        while(line[j] != ' ')
                        {
                           j++;
                        }
                        j++;
                     }
                  }
//printf("before algo\n");
//printMatrix();

                  // algorithm --find greater guy in each row and column
                  mow = 1;
                  for(i=0; i<row; i++)
                  {
                     mow = 1;
                     for(k=0; k<col; k++)
                     {
                        mow = mow * v1[i][k];
                     }

                     if(mow >= 2)
                     {
                        for(k=0; k<col; k++)
                        {
                           v2[i][k] = 2;
                        }
                     }
                     else
                     {
                        for(k=0; k<col; k++)
                        {
                           v2[i][k] = 1;
                        }
                     }
                  }
//printf("after row mow\n");
//printMatrix();

                  // algorithm --find greater guy in each row and column
                  mow = 1;
                  for(i=0; i<col; i++)
                  {
                     mow = 1;
                     for(k=0; k<row; k++)
                     {
                        mow = mow * v1[k][i];
                     }

                     //if(mow >= 2)
                     //{
                     //   for(k=0; k<col; k++)
                     //   {
                     //      v2[k][i] = 2;
                     //   }
                     //}
                     if(mow == 1)
                     {
                        for(k=0; k<row; k++)
                        {
                           v2[k][i] = 1;
                        }
                     }
                  }
//printf("after col mow\n");
printMatrix();  
                
                  // now - if difference exists --pattern doesnt exist
                  for(i=0; i<row; i++)
                  {
                     for(k=0; k<col; k++)
                     {
                        if(v1[i][k] != v2[i][k])
                        {
                            result = 0;
                            break;
                        }
                     }
                  }

                  printf("test=%d result=%d\n", counter, result);
                  sprintf(out,"Case #%u: %s\n",counter,result?"YES":"NO");
                  fputs(out, file1);
//scanf("%d", &j);
             
 } // for loop

}

fclose(file);
fclose(file1);
//fclose(file2);
//fclose(file3);

//scanf("%d", &j);

}


void printMatrix()
{
     int i=0,k=0;
                  for(i=0; i<ROW; i++)
                  {
                     for(k=0; k<COL; k++)
                     {
                        printf("%d ",v1[i][k]);
                     }
                     printf("\n");
                  }
                   printf("\n");
                  for(i=0; i<ROW; i++)
                  {
                     for(k=0; k<COL; k++)
                     {
                        printf("%d ",v2[i][k]);
                     }
                     printf("\n");
                  }

}

void fillMatrix()
{
     int i=0,k=0;
                  for(i=0; i<ROW; i++)
                  {
                     for(k=0; k<COL; k++)
                     {
                        v1[i][k] = 0;
                     }
                  }

                  for(i=0; i<ROW; i++)
                  {
                     for(k=0; k<COL; k++)
                     {
                        v2[i][k] = 100;
                     }
                  }
}
