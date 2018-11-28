#include <stdio.h>
#include <iostream>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int z=1;z<=t;z++)
	{
		int n1,n2,v1[4][4],v2[4][4];
		cin>>n1;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>v1[i][j];
		cin>>n2;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				cin>>v2[i][j];

		n1--;
		n2--;
		int flag = 0,val = 0;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(v1[n1][i] == v2[n2][j])
				{
					flag++;
					val = v1[n1][i];
				}

		switch(flag)
		{
			case 0: printf("Case #%d: Volunteer cheated!\n", z); break;
			case 1: printf("Case #%d: %d\n",z,val ); break;
			default:printf("Case #%d: Bad magician!\n", z); break;
		}
	}
}