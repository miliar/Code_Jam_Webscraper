#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	int t,n1,n2,i,j,k,c,ans;
	cin >> t;
	for(k=1;k<=t;k++)
	{
	
		int arr[4][4];
		int brr[4][4];
		int a[4];
		int b[4];
		cin >> n1;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin >> arr[i][j];
			cin >> n2;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin >> brr[i][j];
		
		for(i=0;i<4;i++)
			a[i]=arr[n1-1][i];
		for(i=0;i<4;i++)
			b[i]=brr[n2-1][i];
		c=0;	
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(a[i]==b[j])
				{
					if(c==0)
						ans=a[i];
					c++;
				}
			}
		}
		if(c==1)
			printf("Case #%d: %d\n",k,ans);
		else if(c>1)
			printf("Case #%d: Bad magician!\n",k);
		else if(c==0)
			printf("Case #%d: Volunteer cheated!\n",k);
	}
		return 0;
}
