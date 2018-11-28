#include <cstdio>
#include <vector>


void solve(int caseNo)
{
	int smax;
	char a[1024];
	std::vector<int> menCount;
	scanf("%d %s", &smax, a);

	for (size_t i = 0; i != (smax+1); i++){
		menCount.push_back(a[i]-'0');
	}
	int myMen = 0;
	int standing = 0;
	for (size_t i = 0; i != (smax+1); i++){
		if (standing < i){
			myMen += (i - standing);
			standing = i;
		}
		standing += menCount[i];
	}


	if (caseNo > 1)
		printf("\n");
	printf("Case #%d: %d", caseNo, myMen);
}

int main()
{
	int numOfTestCases, i;
	scanf("%d", &numOfTestCases);
	for (i = 0; i < numOfTestCases; i++){
		solve(i+1);
	}
}
