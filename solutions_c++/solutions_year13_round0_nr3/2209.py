#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;




int A[1001][1001];
int B[1001][1001];

int isPalindrome(unsigned long long i)
{
	int stack[100];
	int top=0;
	int stack1[100];
	int top1=0;

	unsigned long long j=i;

	while(j>0){

		stack[top++]=j%10;
		j=j/10;
	}

	while(top>=0)
	{
		stack1[top1++]=stack[--top];
	}

	for(int i=0;i<top1;i++)
		if(stack1[i]!=stack[i])
			return 0;

	return 1;



}


int main()
{
	FILE * fin;
    FILE * fout;

	unsigned long long A, B;

	

	fin=fopen("CC-small1.in","r");
	fout=fopen("CC-small.out", "w");

	

	int iter=0;
	unsigned long long res=0;
	
	fscanf(fin,"%d\n", &iter);

		

	for(int j=0;j<iter;j++) {
      
    fscanf(fin, "%llu %llu\n", &A, &B);
	res=0;
	for(unsigned long long i=A;i<=B;i++) {
		
		unsigned long long root= sqrt((double)i);

		if(isPalindrome(i)  && root*root==i && isPalindrome(root))
		{	//printf(" %uul ",i ) ;
		   // printf(" %uul\n", root) ;
		    res++;}

		//&& ((unsigned long long)(sqrt((double)i)))*(unsigned long long (sqrt((double)i)))==i
	} 

	
	fprintf(fout,"Case #%d: %llu\n", j+1, res);
	}
    
	//printf("%d\n",isPalindrome(212));
	//printf("%d\n",isPalindrome(2222222222222222222));
	//printf("%d\n",sizeof(unsigned long));
	fclose(fin);
	fclose(fout);

	return 0;
}

