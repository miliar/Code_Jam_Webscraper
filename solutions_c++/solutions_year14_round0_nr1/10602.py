#include <iostream>
#include <set>
#include <fstream>
#include <stdio.h>
#include <cstdlib>
using namespace std;



int main() {
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	// your code goes here
	int n;
	cin>>n;
	for(int i = 0 ;i<n;i++)
	{
		int g;
		cin>>g;
		int row[4];
		for(int j = 0 ;j<4;j++)
		{
			int arr[4];
			for(int k = 0 ; k<4;k++)
			{
				cin>>arr[k];
			}
			if(j==(g-1))
			{
				for(int x = 0 ; x<4;x++)
					row[x] = arr[x];
			}
		}
		cin>>g;
		for(int j = 0 ;j<4;j++)
		{
			int arr[4];
			for(int k = 0;k<4;k++)
			{
				cin>>arr[k];
			}
			if(j == (g-1))
			{
				set<int> s;
				int ans = 0;
				for(int x = 0;x<4;x++)
				{
					for(int y = 0;y<4;y++)
					{
						if(arr[x]==row[y])
						{
							s.insert(arr[x]);
							ans = arr[x];
						}
					}
				}
				if(s.size() > 1)
					printf("Case #%d: Bad magician!\n",i+1);
				else if (s.size() == 1)
					printf("Case #%d: %d\n",i+1,ans);
				else
					printf("Case #%d: Volunteer cheated!\n",i+1);
			}
		}

	}
	return 0;
}