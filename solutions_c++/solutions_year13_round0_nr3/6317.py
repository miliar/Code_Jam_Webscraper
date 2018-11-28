#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>
using namespace std;

bool IsPol(unsigned long long a)
{
	string test = to_string(a);
	int l = test.length();
	if (l > 1)
	{
		for (int i = 0; i < l/2; i++)
		{
			if(test[i] != test[l-i-1])
				return false;
		} 
	}
	return true;
}

bool IsSquare(unsigned long long a)
{
	double test = sqrt(a);
	if(test - (unsigned long long) test == 0)
		return true;
	else
		return false;
}

void main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);

	int N;
	scanf("%d",&N);

	for(int Case=0;Case<N;Case++)
	{
		unsigned long long A;
		unsigned long long B;
		int answer = 0;
		scanf("%llu %llu",&A,&B);
		
		double lower = sqrt(A);
		unsigned long long lowerBound = (unsigned long long) lower;
		if(lower - lowerBound > 0)
			lowerBound++;
		double upper = sqrt(B);
		unsigned long long upperBound = (unsigned long long) upper;

		for (unsigned long long i = lowerBound; i <= upperBound; i++)
		{
			if(IsPol(i) && IsPol(i*i))
				answer++;
		}

		printf("Case #%d: %d\n",Case+1,answer);
	}
}