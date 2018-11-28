#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>

bool isPalindrome(int num)
{
	char numStr[32];
	sprintf(numStr, "%d", num);
	int len = strlen(numStr);
	int i, j;

	for (i = 0, j =len-1; i<j; i++, j--){
		if (numStr[i] != numStr[j])
			return false;
	}
	return true;
}
int main()
{
	int numOfCases, caseCount = 0;
	int low, high;
	int lowsqrt, highsqrt;
	int value, sqr;
	int i;
	std::vector<int> output;

	scanf("%d", &numOfCases);
	while(caseCount < numOfCases){
		value = 0;
		caseCount++;
		scanf("%d", &low);
		scanf("%d", &high);
		lowsqrt = (int)sqrt(low);
		highsqrt = (int)sqrt(high) + 1;

		for (i = lowsqrt; i <= highsqrt; i++){
			if(isPalindrome(i)) {
				sqr = i*i;
				if(sqr>= low && sqr <= high && isPalindrome(sqr))
					value++;
			}
		}
		output.push_back(value);
	}
	for(size_t i = 0; i< output.size(); i++){
		std::cout<<"Case #" << i+1 << ": " << output[i] <<"\n";
	}
}
