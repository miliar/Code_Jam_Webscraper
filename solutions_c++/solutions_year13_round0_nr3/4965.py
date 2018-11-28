#include <cstdio>
#include <vector>
#include <cmath>

using namespace std;

bool isNumPalindrome(int num)
{
    int tempNum = num;
    int newNum  = 0;

    while (tempNum) {
        int rem = tempNum % 10;
        newNum  = newNum * 10 + rem;
        tempNum /= 10;
    }

    if (num == newNum)
        return true;

    return false;
}

int getSquareRoot(int num)
{
    for (int i = 1; i <= num; i++) {
        if (i * i == num)
            return i;
    }

    return false;
}

int solve(int min, int max)
{
    int count = 0;

    for (int i = min; i <= max; i++) {
        if ( isNumPalindrome(i) && getSquareRoot(i) && isNumPalindrome(getSquareRoot(i)) )
            count++;
    }

    return count;
}

int main()
{
    FILE *fp = fopen("prob_small.in", "r");  
    
    bool special = false;
	int min, max, testcase;
    fscanf(fp, "%d\n", &testcase);


	for (int caseId = 1; caseId <= testcase; caseId++)
	{
        fscanf(fp, "%d ", &min);
        fscanf(fp, "%d",  &max);

        printf("Case #%d: %d\n", caseId, solve(min, max));
        
        fscanf(fp, "\n");
	}
	return 0;
}