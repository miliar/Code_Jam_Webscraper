#include<cstdio>
#include "gmp.h"
//#include "/home/saurabh/Downloads/gmp-5.1.1/gmp.h"

int checkpalindrome(char *arr, int len)
{
	//printf("%s, %d\n", arr, len);
	volatile int i = 0, j = len - 1;
	while((arr[i] == arr[j]) && (i < j))
	{
		i++;
		j--;
	}
	
	if(i < j)
		return -1;
	else
		return 1;
}

int findlength(char* arr)
{
	volatile int i=0;
	while(arr[i++] != '\0');
	//printf("%s, %d\n", arr, i);
	return i-1;
}

int main(int argc, char** argv)
{
	int t = 0;
	FILE *in = fopen(argv[1], "r");
	FILE *out = fopen(argv[2], "w");
	
	mpz_t one;
	mpz_init(one);
	mpz_set_str(one, "1", 10);
	
	fscanf(in, "%d", &t);
	for(int i=1; i<=t; i++)
	{
		mpz_t start, end, root, nextnum;
		mpz_init(start);
		mpz_init(end);
		mpz_init(root);
		mpz_init(nextnum);

		char startnum[1000] = {'\0'}, endnum[1000] = {'\0'};
		fscanf(in, "%s", startnum);
		fscanf(in, "%s", endnum);
		
		mpz_set_str(start, startnum, 10);
		mpz_set_str(end, endnum, 10);

		long count = 0;
		while(mpz_cmp(start, end) <= 0)
		{
			char num[1000] = {'\0'};
			mpz_get_str(&num[0], 10, start);
			
			int res = checkpalindrome(num, findlength(num));
			
			if(res == 1)
			{
				//printf("%s\n", num);
				if(mpz_perfect_square_p(start))
				{
					mpz_init(root);
					mpz_sqrt(root, start);
					char sq_root[1000] = {'\0'};
					mpz_get_str(&sq_root[0], 10, root);
					int res2 = checkpalindrome(sq_root, findlength(sq_root));
					if(res2 == 1)
						count++;
				}
			}
			
			mpz_init(nextnum);
			mpz_add(nextnum, start, one);
			mpz_init_set(start, nextnum);
		}
		
		mpz_clear(start);
		mpz_clear(end);
		mpz_clear(nextnum);
		mpz_clear(root);

		fprintf(out, "Case #%d: %ld\n", i, count);   
	}
	return 0;
}
