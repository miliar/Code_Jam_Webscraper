#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

struct in_case_t
{
	int s_max;
	vector<int> people;
};

int solve(struct in_case_t *ca)
{
	int smax = ca->s_max;
	vector<int> &p = ca->people;

	int up = 0;
	int needed = 0;
	for(int i=0; i<smax+1; i++)
	{
		if(up < i)
		{
			needed += i-up;
			up += i-up;
		}
		up += p[i];
	}
	return needed;
}

int main(int argc, char **argv)
{
	vector<in_case_t> cases;

	printf("Input\n\n");

	FILE *input = fopen(argv[1], "r");

	int n;
	fscanf(input, "%d\n", &n);

	printf("%d\n", n);
	for(int i=0; i<n; i++)
	{
		in_case_t ca;
		fscanf(input, "%d ", &ca.s_max);
		for(int j=0; j<ca.s_max+1; j++)
		{
			unsigned char p;
			fscanf(input, "%c", &p);
			ca.people.push_back((int)(p-48));
		}

		printf("Case #%d: %d ", i, ca.s_max);
		for(int j=0; j<ca.s_max+1; j++)
			printf("%d", ca.people[j]);

		printf("\n");

		cases.push_back(ca);
	}
	fclose(input);
	printf("\n\n");

	FILE *output = fopen("output.txt", "w");

	printf("Output\n\n");

	for(int i=0; i<n; i++)
	{
		int sol = solve(&cases[i]);
		printf("Case #%d: %d\n", i+1, sol);
		fprintf(input, "Case #%d: %d\n", i+1, sol);
	}

	fclose(output);

	return 0;
}