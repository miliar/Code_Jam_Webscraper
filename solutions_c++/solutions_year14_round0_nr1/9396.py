#include <cstdio>

int num[17];

int main(int argc, char const *argv[])
{
	int testcase;

	int frow,srow;
	int a,b,c,d;
	int result;
	int numresult;

	scanf("%d",&testcase);
	for (int i = 1; i <= testcase; ++i)
	{
		for (int xxx = 0; xxx < 17; ++xxx)
		{
			num[xxx] = 0;
		}
		scanf("%d",&frow);
		for (int row = 1; row <= 4; ++row)
		{
			scanf("%d %d %d %d",&a ,&b ,&c ,&d);
			if(row==frow)
			{
				num[a]++;
				num[b]++;
				num[c]++;
				num[d]++;
			}
		}
		result = 0;
		numresult = 0;
		scanf("%d",&srow);
		for (int row = 1; row <= 4; ++row)
		{
			scanf("%d %d %d %d",&a ,&b ,&c ,&d);
			if(row==srow)
			{
				if(num[a]>0)
				{
					numresult++;
					result = a;
				}
				if(num[b]>0)
				{
					numresult++;
					result = b;
				}
				if(num[c]>0)
				{
					numresult++;
					result = c;
				}
				if(num[d]>0)
				{
					numresult++;
					result = d;
				}
			}
		}
		

		printf("Case #%d: ",i );
		if(numresult==0) printf("Volunteer cheated!\n");
		else if(numresult==1) printf("%d\n",result );
		else if(numresult>1) printf("Bad magician!\n");
	}
	return 0;
}