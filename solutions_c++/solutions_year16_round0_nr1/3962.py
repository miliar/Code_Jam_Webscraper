#if 0==0

#include<stdio.h>
#include<vector>
using namespace std;

int main()
{
	FILE *i_fileOut;
	fopen_s(&i_fileOut, "QualA.out", "w");
	int n;
	scanf("%d", &n);
	for (int i_case = 1 ; i_case <= n ; i_case++)
	{
		printf("Case #%d: ", i_case);
		fprintf(i_fileOut, "Case #%d: ", i_case);
		
		int n = 0;
		scanf("%d", &n);
		
		int m = n;
		bool ok = false;

		/*
		while (m > 0)
		{
			if ((m % 10) % 2 == 1) { ok = true; break; } else m /= 10;
		}*/
		ok = (n != 0);

		if (!ok)
		{
			printf("INSOMNIA\n");
			fprintf(i_fileOut, "INSOMNIA\n");
			continue;
		}


		int p = n;
		int s = 0;
		int i_ans = 1;

		vector<short> i_count;
		i_count.resize(10, 0);

		while (true)
		{
			m = p;
			
			while (m > 0)
			{
				if (i_count[m % 10] == 0)
				{
					i_count[m % 10] = 1;
					s++;
					if (s >= 10) break;
				}
				m /= 10;
			}
			
			if (s >= 10) break;
			p += n;
		}
		
		i_ans = p;

		printf("%d\n", i_ans);
		fprintf(i_fileOut, "%d\n", i_ans);
	}

	fclose(i_fileOut);
	return 0;
}

#endif