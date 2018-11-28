# include <cstdio>
# include <iostream>
# define i64 long long
# define INPUT_FILE "A-small-attempt1.in"
# define OUTPUT_FILE "op.txt"
using namespace std;

int main()
{
	i64 T, t, maxS, ans, i;
	char S[1002];
	bool flag;
	FILE *ip, *op;
	
	ip = fopen(INPUT_FILE, "r");
	op = fopen(OUTPUT_FILE, "w");
	fscanf(ip, "%lld", &T);
	//printf("T:%lld\n", T);
	for(t = 1; t <= T; ++t)
	{
		ans = 0;
		flag = false;
		
		fscanf(ip, "%lld", &maxS);
		fscanf(ip, "%s", S);
		
		S[0] = S[0] - '0';
		for(i = 1; i <= maxS; ++i)
		{
			S[i] -= '0';
			flag = S[i] != 0;
			if(S[i - 1] < i && flag)
			{
				//printf("\ti:%lld S[i-1]:%lld\n", i, S[i - 1]);
				ans += i - S[i - 1];
				S[i - 1] += i - S[i - 1];
			}
			S[i] += S[i - 1];
		}
		fprintf(op, "Case #%lld: %d\n", t, ans);
	}
	fclose(ip);
	fclose(op);
	
	return 0;
}
