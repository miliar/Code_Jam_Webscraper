#include <iostream>
#include <cstdbool>
using namespace std;

int updateFound(long int number, bool found[]){
	int updatedCount = 0;
	while(number != 0){
		if (!found[number%10])
		{
			found[number%10] = true;
			updatedCount++;
		}
		number /= 10;
	}
	return updatedCount;
}

int main(){
	//freopen("input.txt", "r");
	//freopen("output.txt", "w");
	int totalCases;	scanf("%d", &totalCases);
	for (int caseNo = 0; caseNo < totalCases; ++caseNo)
	{
		printf("Case #%d: ", caseNo);
		bool found[10];
		int noOfFound = 0;
		//init
		for (int i = 0; i < 10; ++i)
			found[i] = false;
		long int n, multiplier = 0;	scanf("%ld", &n);
		if (n == 0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		while(noOfFound != 10){
			multiplier++;
			noOfFound += updateFound(n*multiplier, found);
		}
		printf("%ld\n", n*multiplier);
	}
	return 0;
}
