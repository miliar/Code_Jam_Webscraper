#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;
int main ()
{
	int no_testcases;
	scanf("%d", &no_testcases);
	
	
	for (int i=1; i<=no_testcases; i++) {
		int ans1, ans2;
		vector<int> row1, row2;
		scanf("%d",&ans1);

		for (int j1 = 0; j1 < 4; ++j1)
		{
			for (int j2 = 0; j2 < 4; ++j2)
			{
				int temp;
				scanf("%d", &temp);
				if(j1+1==ans1){
					row1.push_back(temp);
				}
			}
		}
		scanf("%d",&ans2);
		for (int j1 = 0; j1 < 4; ++j1)
		{
			for (int j2 = 0; j2 < 4; ++j2)
			{
				int temp;
				scanf("%d", &temp);
				if(j1+1==ans2){
					row2.push_back(temp);
				}
			}
		}
		// find no. of common elements in the two vectors row1 and row2
		int no_common = 0;
		int common_elem = 0;
		for (int ii = 0; ii < row1.size(); ++ii)
		{
			int elem1 = row1[ii];
			for (int j = 0; j < row2.size(); ++j)
			{
				int elem2 = row2[j];
				if(elem1 == elem2){
					no_common++;
					common_elem = elem1;
				}
			}
		}
		if (no_common == 0)
		{
			printf("Case #%d: Volunteer cheated!\n",i );
		}
		if (no_common == 1)
		{
			printf("Case #%d: %d\n",i, common_elem);
		}
		if (no_common > 1)
		{
			printf("Case #%d: Bad magician!\n",i );
		}

	}
	
	return 0;
}