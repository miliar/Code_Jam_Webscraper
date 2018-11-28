#include <iostream>
#include <cstdio>
#include <cmath>
#include <time.h>  
using namespace std;



	int K, N;
	int start[201];
	int available[201];
	int needed[201];
	int potavail[201];

	int open[201];
	int contains[201][201];
	int solution[201];
	int fsolution[201];
	int used[201];
	int solved=0;
	int tryall=0;
	time_t timer;

void backtrack(int size, int N)
{
	int totavail=0;
	if(solved)
		return;

	if(difftime(time(NULL),timer)>20)
		return;

   for(int i=0;i<=200;i++)
		totavail+=available[i];

   if(totavail<=0 && size<N)
	   return;

	
	for(int i=0;i<=200;i++){
		potavail[i]=available[i];
		needed[i]=0;
	}

	for(int i=1;i<=N;i++)
	{
		if(used[i]==0){
		for(int j=1;j<=contains[i][0];j++){
			potavail[contains[i][j]]++;
		}
				
		needed[open[i]]++;
		}
	}

	for(int i=1;i<=200;i++)
	{
		if(potavail[i]<needed[i] && size<N)
			return;
	}
		

	if(size==N)
	{
		printf("Solved: ");

		for(int i=1;i<=N;i++){
			printf("%d ",solution[i]);
			if(solved==0){
			fsolution[i]=solution[i];
			}
		}
		solved=1;
		printf("\n");		

	}

	for(int i=1;i<=N;i++){
		if(available[open[i]]>0 && used[i]==0){
			solution[size+1]=i;
			used[i]=1;
			available[open[i]]--;
			for(int j=1;j<=contains[i][0];j++){
				available[contains[i][j]]++;
			}
			
			/*printf("Trying solution: ");
			for(int j=1;j<=size+1;j++)
			{
				printf("%d ", solution[j]);
			}
			printf("\n");*/
			
			
			backtrack(size+1,N);

			solution[size+1]=0;
			used[i]=0;
			available[open[i]]++;

			for(int j=1;j<=contains[i][0];j++){
				available[contains[i][j]]--;
			}
		
		}

	}
	

}



int main()
{
	FILE * fin;
    FILE * fout;

	

	for(int i=0;i<=200;i++) {available[i]=0; potavail[i]=0; needed[i]=0; start[i]=0;}
	for(int i=0;i<=200;i++) {

	for(int j=0;j<=200;j++)contains[i][j]=0;
	
	fsolution[i]=0; 
	solution[i]=0;
	open[i]=0;
	used[i]=0;
	}
	

	fin=fopen("DD-small14.in","r");
	fout=fopen("DD-small.out", "w");

	

	int iter=0;
	
	
	fscanf(fin,"%d\n", &iter);
	//printf("%d\n\n", iter);
		

	for(int j=0;j<iter;j++) {

	
  

    time(&timer);  /* get current time; same as: timer = time(NULL)  */

  

	for(int i=0;i<=200;i++) {available[i]=0; start[i]=0; needed[i]=0; potavail[i]=0;}
	for(int i=0;i<=200;i++) {

	for(int j=0;j<=200;j++)contains[i][j]=0;
	
	fsolution[i]=0; 
	solution[i]=0;
	open[i]=0;
	used[i]=0;
	}

    solved=0;
	K=0;
	N=0;

	//printf("\nIter %d\n", j+1);
    fscanf(fin, "%d %d\n", &K, &N);
	printf("K:%d N:%d\n", K, N);
	for(int i=1;i<=K;i++)
	{
		 fscanf(fin, "%d ", &start[i]);
		 available[start[i]]++;
	}
	

	for(int i=1;i<=N;i++)
	{
		fscanf(fin, "%d", &open[i]);
		fscanf(fin, "%d", &contains[i][0]);

		for(int j=1;j<=contains[i][0];j++) {

			if(j==contains[i][0]){
				fscanf(fin, "%d\n", &contains[i][j]);
				break;
			}
			fscanf(fin, "%d", &contains[i][j]);
			

		}

		
	}

	
	
	//Print 

	
	for(int i=1;i<=K;i++)
	{
		 printf("%d ", start[i]);

		 if(i==K)printf("\n");
		
	}
	

	for(int i=1;i<=N;i++)
	{
		printf("%d ", open[i]);
		printf("%d ", contains[i][0]);

		for(int j=1;j<=contains[i][0];j++) {

			if(j==contains[i][0]){
				printf("%d\n", contains[i][j]);
			    break;
			}
			printf("%d ", contains[i][j]);

			

		}

		if(contains[i][0]==0)
			printf("\n");

		
		
	}

	printf("\n");
	
	

	backtrack(0,N);

	if(solved){

	fprintf(fout,"Case #%d: ", j+1);
	for(int i=1;i<N;i++)
		fprintf(fout,"%d ", fsolution[i]);

	fprintf(fout,"%d\n", fsolution[N]);

	}
	else
	{   printf("Case #%d: IMPOSSIBLE\n", j+1);
		fprintf(fout,"Case #%d: IMPOSSIBLE\n", j+1);
	}
	}
    
	
	fclose(fin);
	fclose(fout);

	return 0;
}

