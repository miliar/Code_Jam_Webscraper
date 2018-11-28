#include <iostream>
#include <fstream>
#include <vector>
#include <cstdio>

using namespace std;


int main(){
	int tests;
	scanf("%d", &tests);

	for(int i = 0; i < tests; ++i){
		int row, temp;
		int nums[4];
		int nums2[4];

		scanf("%d", &row);

		for(int j = 1; j <= 4; ++j)
			if(j == row)
				scanf("%d %d %d %d", &nums[0], &nums[1], &nums[2], &nums[3]);
			else
				scanf("%d %d %d %d", &temp, &temp, &temp, &temp);

		scanf("%d", &row);

		for(int j = 1; j <= 4; ++j)
			if(j == row)
				scanf("%d %d %d %d", &nums2[0], &nums2[1], &nums2[2], &nums2[3]);
			else
				scanf("%d %d %d %d", &temp, &temp, &temp, &temp);

		vector<int> sol;

		for(int j = 0; j < 4; ++j)
			for(int k = 0; k < 4; ++k)
				if(nums[j] == nums2[k])
					sol.push_back(nums[j]);

		if(sol.size() == 1)
			printf("Case #%d: %d\n", i + 1, sol[0]);
		else if(sol.empty())
			printf("Case #%d: Volunteer cheated!\n", i + 1);
		else 
			printf("Case #%d: Bad magician!\n", i + 1);
	}
}