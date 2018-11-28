#include <iostream>
using namespace std;
bool a[16];

int main() {
	int t,caseno=1;
	scanf("%d",&t);
	while(t--)
	{
		for(int i=0;i<16;i++)
		{
			a[i]=false;
		//	b[i]=false;
		}
		//First case
		int n;
		scanf("%d",&n);
		int temp,limit=4*(n-1);
		for(int i=0;i<limit;i++)
			{
				scanf("%d",&temp);
			}
		for(int i=limit;i<(limit+4);i++)
			{
				scanf("%d",&temp);
				a[temp-1]=true;
			//	b[temp-1]=true;
			}
		for(int i=(limit+4);i<16;i++)
			{
				scanf("%d",&temp);
			}
		
		//
		
	/*	for(int i=0;i<16;i++)
			cout<<a[i]<<" ";*/
		//Second Cse
		
		scanf("%d",&n);
	limit=4*(n-1);
		for(int i=0;i<limit;i++)
			{
				scanf("%d",&temp);
				a[temp-1]=false;
			}
		for(int i=limit;i<(limit+4);i++)
			{
				scanf("%d",&temp);
				
			}
		for(int i=(limit+4);i<16;i++)
			{
				scanf("%d",&temp);
				a[temp-1]=false;
			}
			int count=0;
			int index=0;
		for(int i=0;i<16;i++)
		{
			if(a[i])
				{
					count++;
					index=i+1;
				}
		}
	//	cout<<endl;
	/*	for(int i=0;i<16;i++)
			cout<<a[i]<<" ";*/
		if(count==1)
			printf("Case #%d: %d\n",caseno++,index);
		else if(count==0)
			printf("Case #%d: Volunteer cheated!\n",caseno++);
		else
			printf("Case #%d: Bad magician!\n",caseno++);
		
	}
	return 0;
}