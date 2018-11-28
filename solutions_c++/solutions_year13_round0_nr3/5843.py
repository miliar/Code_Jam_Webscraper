#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<vector>
#include<string>
using namespace std;


int is_fair(long double x)
{
	char str[100];
	int i,j,len;

	sprintf(str,"%.0Lf",x);

	len = strlen(str);

	for(i=0; i<len/2; i++)
		if(str[i] != str[len-1-i])
			return 0;

	return 1;
}

int fair[10000005];

main()
{
	int T,CASE=0;
	int i,j,k;
	char buf[1000];
	long double A,B,x;


	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);

//	freopen("C-large.in","r",stdin);
//	freopen("C-large.out","w",stdout);

	for(i=1; i<10000005; i++)
	{
		if(is_fair(i))
			fair[i] = 1;
		else
			fair[i] = 0;
	}


	scanf("%d",&T);

	while(T--)
	{
		CASE++;

		scanf("%Lf %Lf",&A,&B);

		k = 0 ;
		for(x=1; x<10000005; x++)
		{
			if(fair[(int)x])
			{
				if(x*x >= A && x*x <= B)
					if( is_fair(x*x) )
						k++;
			}

		}

		printf("Case #%d: %d\n",CASE,k);


	}




}