#include <iostream>
#include <cstdio>
#include <cstring>
#include <conio.h>>
using namespace std;

int main()
{
	
 freopen("A-small-attempt0.out","w",stdout);
 freopen("A-small-attempt0.in","r",stdin); 	
 int NuTest,magicianNum1,magicianNum2;
 int mat1[4][4],mat2[4][4];
 scanf("%d",&NuTest);
 int counter=1;
 while(counter<=NuTest)
 {
   scanf("%d",&magicianNum1);
   for(int i=0;i<4;++i)
    for(int j=0;j<4;++j)
     scanf("%d",&mat1[i][j]);
     
   scanf("%d",&magicianNum2);
   for(int i=0;i<4;++i)
    for(int j=0;j<4;++j)
     scanf("%d",&mat2[i][j]);
   
   int t=0;
   int flag=0;
   for(int i=0;i<4;++i){
    for(int j=0;j<4;++j){
	     if(mat1[magicianNum1-1][i]==mat2[magicianNum2-1][j])
	     {		   
	      flag+=1;
	      t=mat1[magicianNum1-1][i];
	     }
 		}
   }
   if(flag==1)
	printf("Case #%d: %d\n",counter,t);
   else if(flag>1)
        printf("Case #%d: Bad magician!\n",counter);
   else
	printf("Case #%d: Volunteer cheated!\n",counter);        

   counter+=1; 
 }	

}
