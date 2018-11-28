#include <stdio.h>


int main()
{
	FILE* fin;
	int t;
	int i;
	int j;
	int k;
		
	fin = fopen("in.txt", "rb");
	freopen("out.txt", "wb", stdout);

	fscanf(fin, "%d\n", &t);
	
	
	{
		for(i = 0; i < t; i++)
		{
			char s[1024] = {0};
			char l[1024] = {0};

			fscanf(fin, "%s\n", s);

			l[0] = s[0];

			for(j = 0; s[j]; j++)
				if(s[j] < l[0])
					l[j] = s[j];
				else
				{
					for(k = j; 0 < k; k--)
						l[k] = l[k - 1];

					l[0] = s[j];
				}

			printf("Case #%d: %s\r\n", i + 1, l);
		}
	}

	fclose(fin);

	return 0;
}
