#include <iostream>
#include <algorithm>
#include<cstdio>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int ind=0;ind<t;ind++)
	{
		int a1,a2,arr1[4],arr2[4],key;
		cin>>a1;
		a1--;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				int temp;
				cin>>temp;
				if(i==a1)
				{
					arr1[j]=temp;
				}
			}
		cin>>a2;
		a2--;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
			{
				int temp;
				cin>>temp;
				if(i==a2)
					arr2[j]=temp;
			}
		sort(arr2,arr2+4);
		int count=0;
		for(int i=0;i<4;i++)
			if(binary_search(arr2,arr2+4,arr1[i]))
			{
				count++;
				key=i;
			}
		printf("Case #%d: ",ind);
		if(count==0)
			printf("Volunteer cheated!\n");
		else if(count==1)
			printf("%d\n",arr1[key]);
		else
			printf("Bad magician!\n");
	}
	return 0;
}
