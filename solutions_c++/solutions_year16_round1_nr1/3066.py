#include <iostream>
#include <vector>
#include <string>
#include <cmath>

#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)

int compare(const void *x, const void *y)
{
	return (*(int*)x - *(int*)y);
}

using namespace std;

int main()
{
	FILE* input;
	FILE* output;

	input = fopen("C:\\Users\\현우\\Desktop\\Google\\2016R1A\\Problem A\\large.txt", "r");
	output = fopen("C:\\Users\\현우\\Desktop\\Google\\2016R1A\\Problem A\\large_answer.txt", "w");

	int T;

	int t = 1;

	fscanf(input, "%d", &T);

	while (T >= t)
	{
		char S[1001];
		vector<char> L;

		fscanf(input, "%s", S);
		
		L.push_back(S[0]);

		for (int i = 1; S[i] != '\0'; ++i)
		{
			if (L[0] <= S[i])
				L.insert(L.begin(), S[i]);

			else
				L.push_back(S[i]);
		}

		fprintf(output, "Case #%d: ",t);
		for (int i = 0; i < L.size(); ++i)
			fprintf(output, "%c", L[i]);

		fprintf(output, "\n");

		++t;



	}

	return 0;

}