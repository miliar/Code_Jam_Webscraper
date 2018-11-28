#include<stdio.h>
#include<stdlib.h>
#define PAUSE system("pause")
#define MAX 100
int Num[MAX],Now[MAX*2];
int Rec[1000][MAX],End;
int Left[MAX],Right[MAX];
char Input[MAX+1];
bool Palindrome(int *A)
{
	int i,j;
	for(j=MAX-1;j>=0 && A[j]==0;j--);
	if(j<0) return 0;
	for(i=0;i<=j/2;i++)
		if(A[i]!=A[j-i]) return 0;
	return 1;
}
void Square()
{
	int i,j;
	for(i=0;i<MAX*2;i++) Now[i]=0;
	for(i=0;i<MAX;i++)
		for(j=0;j<MAX;j++)
			Now[i+j]+=Num[i]*Num[j];
	for(i=0;i<MAX;i++)
		if(Now[i]>9)
		{
			Now[i+1]+=Now[i]/10;
			Now[i]%=10;
		}
	for(i=MAX;i<MAX*2;i++)
		if(Now[i]) return;
	if(Palindrome(Now))
	{
		for(i=0;i<MAX;i++)
			Rec[End][i]=Now[i];
		End++;
/*		
		printf("#%d:  ",End);
		for(i=MAX-1;i>=0 && Now[i]==0;i--);
		for(;i>=0;i--) putchar(Now[i]+'0');
		puts("");
*/
	}
}
void Find_Answer(int i,int D)
{
	if(i==D) return;
	if(i>0 && Num[i-1]!=0) Square();
	for(int k=9;k>=0;k--)
	{
		Num[i]=k;
		if(Palindrome(Num)) Find_Answer(i+1,D);
	}
}
void GetNumber(int *A)
{
	int i,j,k;
	scanf("%s",Input);
	for(j=0;Input[j];j++);
	for(i=0;i<MAX;i++) A[i]=0;
	for(i=0;i<j;i++) A[i]=Input[j-1-i]-'0';
}
bool Cmp(int *A,int *B)
{
	int i,j;
	for(i=MAX-1;i>=0 && A[i]==0;i--);
	for(j=MAX-1;j>=0 && B[j]==0;j--);
	if(i!=j) return i<j;
	for(;i>=0;i--)
		if(A[i]!=B[i]) return A[i]<B[i];
	return 1;
}
main()
{
//	freopen("C_small.in","r",stdin);
//	freopen("C_small_out.txt","w",stdout);

	int Test,Case,i,j,k,n;
	Find_Answer(0,100);
	scanf("%d",&Test);
	for(Case=1;Case<=Test;Case++)
	{
		GetNumber(Left);
		GetNumber(Right);
		for(n=i=0;i<End;i++)
			if(Cmp(Left,Rec[i]) && Cmp(Rec[i],Right)) n++;
		printf("Case #%d: ",Case);
		printf("%d\n",n);
	}
}
