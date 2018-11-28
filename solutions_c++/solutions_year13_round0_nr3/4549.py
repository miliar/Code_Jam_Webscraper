#include <stdio.h>
#include <vector>
#include <math.h>

#define FILENAME "C-small-attempt0.in"

bool IsPalindrome(int i)
{
	std::vector<char> v;
	while(i)
	{
		v.push_back(i%10);
		i /= 10;
	}
	
	for(int index = 0; index < v.size()/2; ++index)
	{
		if(v[index] != v[v.size()-1-index])
			return false;
	}
	
	return true;
}

void main()
{
	FILE *fIn = fopen(FILENAME, "rb");
	FILE *fOut = fopen("QR_C_out.txt", "wb");

	int T;
	fscanf(fIn, "%d", &T);
	for(int t = 1; t <= T; ++t)
	{
		int A, B;
		fscanf(fIn, "%d %d", &A, &B);

		int start, end;
		float Temp = sqrt((float)A);
		if((int)Temp * (int)Temp < A)
			start = (int)Temp + 1;
		else
			start = (int)Temp;

		Temp = sqrt((float)B);
		if((int)Temp * (int)Temp > B)
			end = (int)Temp - 1;
		else
			end = (int)Temp;

		unsigned int sum = 0;
		for(int i = start; i <= end; ++i)
		{
			if(IsPalindrome(i) && IsPalindrome(i*i))
				++sum;
		}

		fprintf(fOut, "Case #%d: %d\r\n", t, sum);
	}
}