#include<iostream>
#include<cstdio>
#include<cstdlib>
using namespace std;

int ans1;
int ans2;
int mat1[4][4];
int mat2[4][4];

FILE* ptr;
FILE* ptr2;


void test(int n)   //n is the count of test case
{
	fscanf(ptr,"%d",&ans1);
	register int i,j;
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			fscanf(ptr,"%d",&mat1[i][j]);
	fscanf(ptr,"%d",&ans2);
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			fscanf(ptr,"%d",&mat2[i][j]);
	int count=0;
	int ans=0;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if( mat1[ans1-1][i]==mat2[ans2-1][j] )
			{
				count++;
				ans=mat1[ans1-1][i];
			}
		}
	}
	if(count==0)
	{
		fprintf(ptr2,"Case #%d: Volunteer cheated!\n",n);
		printf("Case #%d: Volunteer cheated!\n",n);
	}
	else if(count>1)
	{
		fprintf(ptr2,"Case #%d: Bad magician!\n",n);
		printf("Case #%d: Bad magician!\n",n);
	}
	else if(count==1)
	{
		fprintf(ptr2,"Case #%d: %d\n",n,ans);
		printf("Case #%d: %d\n",n,ans);
	}
}

int main()
{
	char filename[100];
	cout<<"Enter the file name:";
	cin>>filename;
	ptr=fopen(filename,"r");
	ptr2=fopen("out.txt","w");
	int T;
	fscanf(ptr,"%d",&T);
	cout<<"Number of test cases:"<<T<<endl;
	int n;
	for(n=0;n<T;n++)
		test(n+1);
	return 0;
}
