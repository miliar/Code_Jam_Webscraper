#include <stdio.h>
#include <string.h>

__int64 ans[40] = {0,1,
2,
3,
11,
22,
101,
111,
121,
202,
212,
1001,
1111,
2002,
10001,
10101,
10201,
11011,
11111,
11211,
20002,
20102,
100001,
101101,
110011,
111111,
200002,
1000001,
1001001,
1002001,
1010101,
1011101,
1012101,
1100011,
1101011,
1102011,
1110111,
1111111,
2000002,
2001002};

int main()
{
	int T;
	FILE* fp = fopen("C-large-1.in","r");
	FILE* fp1 = fopen("C-large-1.out","w");
	fscanf(fp,"%d",&T);
	for(int c = 1;c <= T;c++)
	{	
		__int64 a,b;
		fscanf(fp,"%I64d %I64d",&a,&b);
		int cnt = 0;
		for(int i = 1;i <= 39;i++)
		{
			__int64 tmp;
			tmp = ans[i]*ans[i];
			if(tmp >= a && tmp <= b)
				cnt++;
		}
		fprintf(fp1,"Case #%d: %d\n",c,cnt);
	}
	fclose(fp);
	fclose(fp1);
	return 0;
}