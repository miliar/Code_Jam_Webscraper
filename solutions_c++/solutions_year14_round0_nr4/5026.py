#include <cstdio>

using namespace std;

void bubble_sort(float a[],int n)
{
	for(int i=0;i<n;i++)
	printf("%f\t",a[i]);
	printf("\n");
	float temp;
    for(int i=1;i< n;i++)
    {
         for(int j=0;j< n-1;j++)
         if(a[j]>a[j+1])
               {
               temp=a[j];
               a[j]=a[j+1];
               a[j+1]=temp;
               }
    }
	for(int i=0;i<n;i++)
	printf("%f\t",a[i]);
	printf("\n");
}

int main()
{

	FILE *fp;
	fp=fopen("C:/Users/prabhusa/Desktop/ans.txt", "w");
	int T;
	scanf("%d",&T);
	for (int test=1;test<=T;test++) {
		int N,dcnt=0,ncnt=0;
		scanf("%d",&N);
		float nao[N],ken[N];
		for(int i=0;i<N;i++)
		{	scanf("%f",&nao[i]);	}
		for(int i=0;i<N;i++)
		{	scanf("%f",&ken[i]);	}
		bubble_sort(nao,N);
		bubble_sort(ken,N);
		int ke=0,na=0;
		for(int i=0;i<N;i++)
		{
			if(nao[N-1-na]>ken[N-1-ke])
			{	
				printf("%f %f\n",nao[N-1-na],ken[N-1-ke]);
				na++; dcnt++;
			}
			else
			{ na++; ke++;}	
		}
		ke=na=0;
		for(int i=0;i<N;i++)
		{
			if(nao[na]<ken[ke])
			{	na++; }
			else
			{ na++; ke++; ncnt++;}	
		}
		fprintf(fp,"Case #%d: %d %d\n",test,ncnt,dcnt);
	}
}
	
