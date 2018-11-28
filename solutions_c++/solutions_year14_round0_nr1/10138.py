#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;


int main(void)
{
	int runs; 
	scanf("%d", &runs);
	for(int run = 1; run <= runs; run++) {
		int arr[17] = {0};
		
		int first, second;
		vector<int> intersection;
		scanf("%d", &first);

		int row[4];
		for(int i = 1; i <= 4; i++) {
			for(int j = 0; j < 4; j++) { 
				scanf("%d", &row[j]);
				if(i == first) {
					arr[row[j]] = 1;
				}
			}
		}


		scanf("%d", &second);

		for(int i = 1; i <= 4; i++) {
			for(int j = 0; j < 4; j++) { 
				scanf("%d", &row[j]);
				if(i == second && arr[row[j]]) {
					intersection.push_back(row[j]);
				} 
			}
		}

		int len = intersection.size();
		switch(len) {
		case 0: 
			printf("Case #%d: %s\n", run, "Volunteer cheated!");
			break;
		case 1:
			printf("Case #%d: %d\n", run, intersection[0]);
			break;
		default:
			printf("Case #%d: %s\n", run, "Bad magician!");
		}
	}
}