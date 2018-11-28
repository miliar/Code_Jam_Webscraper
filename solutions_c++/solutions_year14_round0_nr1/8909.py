#include <cstdio>
#include <vector>
using namespace std;

int main() {
	int numberOfTestCases,firstRow,secondRow,temp;
	scanf("%i",&numberOfTestCases);
	for (int k = 1; k < numberOfTestCases + 1; ++k) {
		vector <int> one;
		vector <int> two;
		vector <int> both;
		scanf("%i",&firstRow);
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				scanf("%i",&temp);
				if ( i + 1 == firstRow ) {
					one.push_back(temp);
				}
			}		
		}
		scanf("%i",&secondRow);
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				scanf("%i",&temp);
				if ( i + 1 == secondRow ) {
					two.push_back(temp);
				}
			}
		}
		for (int i = 0; i < 4; ++i) {
			for (int j = 0; j < 4; ++j) {
				if ( one[i] == two[j] )
					both.push_back(one[i]);
			}
		}
		printf("Case #%i: ",k);
		if ( both.size() == 0 )
			printf("Volunteer cheated!\n");
		else if ( both.size() == 1)
			printf("%i\n",both[0]);
		else
			printf("Bad magician!\n");	
	}
	return 0;
}