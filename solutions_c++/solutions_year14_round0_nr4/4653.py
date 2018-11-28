#include<cstdio>
#include<algorithm>
using namespace std;

int n;
double A[1005];
double B[1005];
int ans1,ans2;
void normal();
void deceitful();

int main()
{
	int tc;
	
	scanf("%d",&tc);
	for(int t=1;t<=tc;t++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%f",&A[i]);
		for(int i=0;i<n;i++)
			scanf("%f",&B[i]);
			
		sort(A,A+n);
		sort(B,B+n);		
		
		normal();
		deceitful();
		printf("Case #%d: %d %d\n",t,ans1,ans2);
	}
	
	
}

void deceitful()
{
	int indexA=0,indexB=0;
	ans1=0;
	while(indexA!=n)
	{
		if(B[indexB]>A[indexA])
		{
			indexA++;
		}
		else
		{
			indexA++;
			indexB++;
			ans1++;
		}
	}
	
	
}


void normal()
{
	int indexA=0,indexB=0;
	while(indexB!=n)
	{
		if(A[indexA]>B[indexB])
		{
			indexB++;
		}
		else
		{
			indexA++;
			indexB++;
		}
	}
	ans2=n-indexA;
	
}





