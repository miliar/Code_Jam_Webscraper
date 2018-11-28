#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
	int	numOfmatch,answer,n,i=0,j;
	freopen("g:/input.txt","r",stdin);
    freopen("g:/output.txt","w",stdout);

    int ans1,ans2,a[4][4],b[4][4];
	cin>>n;
	for(int index=0;index<n;)
	{
		numOfmatch  = 0;
		cin>>ans1;
		ans1--;
		for(i=0 ; i<4 ;i++)
			for(j=0 ; j<4 ;j++)
			cin>>a[i][j];

		cin>>ans2;
		ans2--;
		for(i=0 ; i<4 ;i++)
			for(j=0 ; j<4 ;j++)
			cin>>b[i][j];
	for(i=0 ; i<4 ;i++)
		for(j=0 ; j<4 ;j++)
			{
			if(a[ans1][i] == b[ans2][j])
				{
				numOfmatch++;
				if(numOfmatch == 1)
					answer = a[ans1][i];
				}
			}

		printf("Case #%d: ",++index);
		if(numOfmatch == 0)
			printf("Volunteer cheated!\n");
		else if(numOfmatch == 1)
			printf("%d\n",answer);
		else
			printf("Bad magician!\n");
	}
	return 0;
}
