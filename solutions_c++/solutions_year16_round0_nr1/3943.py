#include <cstdio>
#include <iostream>

using namespace std;

int main()
{
	int N, T;
	unsigned long long tmp;
	char buf[10000];
	bool appear[10], sleep;
	int i, j, k;
	FILE * fin, *fout;
	fin = fopen("input.txt", "r");
	fout = fopen("output.txt", "w");
	
	fscanf(fin, "%d", &T);
	for(i = 1 ; i <= T ; i++)
	{
		sleep = false;
		for(j = 0 ; j < 10 ; j++)
		{	appear[j] = 0;	}
		fscanf(fin, "%d", &N);
		if(N == 0)
		{	}
		else
		{
			for(j = 1 ; sleep == false ; j++)
			{
				sleep = true;
				tmp = N * j;
				sprintf(buf,"%ull", tmp);
				for(k = 0 ; buf[k] != '\0' ; k++)
				{	appear[buf[k] - 48] = true;	}
				for(k = 0 ; k < 10 ; k++)
				{
					if(appear[k] == false)
					{	sleep = false;	break;	}
				}
				if(sleep)
				{	break;	}
			}
		}
		fprintf(fout, "Case #%d: ", i);
		if(sleep)
		{	fprintf(fout, "%d\n", tmp);	}
		else
		{	fprintf(fout, "INSOMNIA\n");	}
	}
	
	return 0;
}