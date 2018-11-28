#include <stdio.h>

void calc_frq(int* frq, char* s)
{
	while(*s)
	{
		if(*s != '.')
			frq[(*s - 'A')]++;

		s++;
	}
}

void eliminate(int* frq, char* s, char c, int n)
{
	while(*s)
	{
		if(*s == c && n)
		{
			frq[(*s - 'A')]--;
			*s = '.';
			n--;
		}

		s++;
	}
}

int compose_1(int* frq, char* s, int* n)
{
	if(frq[25])
	{
		n[0]++;
		eliminate(frq, s, 'Z', 1);
		eliminate(frq, s, 'E', 1);
		eliminate(frq, s, 'R', 1);
		eliminate(frq, s, 'O', 1);

		return 1;
	}
	else if(frq[22])
	{
		n[2]++;
		eliminate(frq, s, 'T', 1);
		eliminate(frq, s, 'W', 1);
		eliminate(frq, s, 'O', 1);

		return 1;
	}
	else if(frq[20])
	{
		n[4]++;
		eliminate(frq, s, 'F', 1);
		eliminate(frq, s, 'O', 1);
		eliminate(frq, s, 'U', 1);
		eliminate(frq, s, 'R', 1);

		return 1;
	}
	else if(frq[23])
	{
		n[6]++;
		eliminate(frq, s, 'S', 1);
		eliminate(frq, s, 'I', 1);
		eliminate(frq, s, 'X', 1);

		return 1;
	}
	else if(frq[6])
	{
		n[8]++;
		eliminate(frq, s, 'E', 1);
		eliminate(frq, s, 'I', 1);
		eliminate(frq, s, 'G', 1);
		eliminate(frq, s, 'H', 1);
		eliminate(frq, s, 'T', 1);

		return 1;
	}

	return 0;
}

int compose_2(int* frq, char* s, int* n)
{
	if(frq[7])
	{
		n[3]++;
		eliminate(frq, s, 'T', 1);
		eliminate(frq, s, 'H', 1);
		eliminate(frq, s, 'R', 1);
		eliminate(frq, s, 'E', 2);

		return 1;
	}
	else if(frq[5])
	{
		n[5]++;
		eliminate(frq, s, 'F', 1);
		eliminate(frq, s, 'I', 1);
		eliminate(frq, s, 'V', 1);
		eliminate(frq, s, 'E', 1);

		return 1;
	}
	else if(frq[18])
	{
		n[7]++;
		eliminate(frq, s, 'S', 1);
		eliminate(frq, s, 'E', 2);
		eliminate(frq, s, 'V', 1);
		eliminate(frq, s, 'N', 1);

		return 1;
	}

	return 0;
}

int compose_3(int* frq, char* s, int* n)
{
	if(frq[8])
	{
		n[9]++;
		eliminate(frq, s, 'N', 2);
		eliminate(frq, s, 'I', 1);
		eliminate(frq, s, 'E', 1);

		return 1;
	}
	else if(frq[14])
	{
		n[1]++;
		eliminate(frq, s, 'O', 1);
		eliminate(frq, s, 'N', 1);
		eliminate(frq, s, 'E', 1);

		return 1;
	}

	return 0;
}

int main()
{
	FILE* fin;
	int t;
	int i;
	int j;
			
	fin = fopen("in.txt", "rb");
	freopen("out.txt", "wb", stdout);

	fscanf(fin, "%d\n", &t);
	{
		for(i = 0; i < t; i++)
		{
			char s[2001] = "";
			int frq[26] = {0};
			int n[10] = {0};

			fscanf(fin, "%s\n", s);

			calc_frq(frq, s);

			while(compose_1(frq, s, n));
			while(compose_2(frq, s, n));
			while(compose_3(frq, s, n));

			printf("Case #%d: ", i + 1);
			for(j = 0; j < 10; j++)
				while(n[j])
				{
					printf("%d", j);
					n[j]--;
				}
			printf("\r\n");
		}
	}

	fclose(fin);

	return 0;
}
