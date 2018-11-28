#include <stdio.h>
#include <vector>


using namespace std;


#define tnum unsigned long long



bool palind(tnum  x)
{
	tnum n[100];
	
	int len = 0;

	while (x > 0)
	{
		n[len++] = x % 10;
		x /= 10;
	}

	len--;

	for (int i = 0; i <= len / 2; i++)
	{
		if (n[i] != n[len-i])
		{
			return false;
		}
	}

	return true;
}

int main()
{
	vector<tnum> palinds;

	FILE *fin =  fopen("in.txt", "r");
	FILE *fout = fopen("out.txt", "w");

	for (tnum i = 0; i < 10000000; i++)
	{
		tnum k = i * i;
		if (palind(k) && palind(i))
		{
			palinds.push_back(k);
		}
	}

	for (auto it = palinds.begin(); it != palinds.end(); it++)
	{
		printf("%lld\n", *it);
	}
	int T;
	fscanf(fin,"%d\n",&T);

	for (int i = 0; i < T; i++)
	{
		int A;
		int B;

		fscanf(fin,"%d %d", &A, &B);

		int count = 0;

		for (auto it = palinds.begin(); it != palinds.end(); it++)
		{
			if (*it >= A && *it <= B)
			{
				count++;
			}
		}

		printf("Case #%d: %d\n", i + 1, count);
		fprintf(fout,"Case #%d: %d\n", i + 1, count);
	}
	//for(int i = 0; i < 10000; i++)
	//{
	//	if (palind(i))
	//	{
	//		printf("%d\n", i);
	//	}
	//}
	fclose(fin);
	fclose(fout);
	return 0;
}