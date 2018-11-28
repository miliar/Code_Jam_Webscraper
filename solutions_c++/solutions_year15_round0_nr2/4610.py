#include<stdio.h>
#include<vector>
#include<algorithm>

using std::vector;

int main()
{
	vector<int> p;
	FILE *i_fileOut;
	fopen_s(&i_fileOut, "QualB.out", "w");
	int n;
	scanf("%d", &n);
	for (int i_case = 1 ; i_case <= n ; i_case++)
	{
		printf("Case #%d: ", i_case);
		fprintf(i_fileOut, "Case #%d: ", i_case);
		
		int d = 0;

		scanf("%d", &d);

		int i_current = 0;
		int i_ans = 0;

		p.resize(d);

		int i_max = 0;

		for (int i = 0 ; i < d ; i++)
		{
			scanf("%d", &p[i]);
			if (p[i] > i_max) i_max = p[i];
		}

//		sort(p.begin(), p.end());
		i_ans = i_max;

		int t;

		for (int i = 1 ; i <= i_max ; i++)
		{
			t = i;
			for (int j = 0 ; j < d ; j++)
			{
				t += (p[j] - 1) / i;				
			}
			if (t < i_ans) i_ans = t;
		}

		printf("%d\n", i_ans);
		fprintf(i_fileOut, "%d\n", i_ans);
	}

	fclose(i_fileOut);
	return 0;
}