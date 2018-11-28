#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int T,n;
double Man[40000],women[40000];
bool now[1400],now1[1400];


int search1(){
	bool can;
	int i,j;
	int number1 = 0;
	for ( i = 0; i < n; ++i )
		{
			can = 0;
			for ( j = 0; j < n; ++j )
				if ( Man[i] > women[j] && now[j] == 0 )
				{
					now[j] = 1; can = 1;break;
				}
			if ( can == 1 ) ++ number1;
		}
	return number1;
}

int search2()
{
	bool can;
	int i,j;
	int number2 = 0;
	for (  i = 0; i < n; ++i )
		{
			can = 0;
			for (  j = 0; j < n; ++j )
				if ( women[j] > Man[i] && now1[j] == 0 )
				{
					now1[j] = 1; can = 1; break;
				}
			if ( can == 0 ) ++number2;
		}
		return number2;
}

void work( int cas){
	    scanf("%d",&n);
	    int i;
		for ( i = 0; i < n; ++i )
			scanf("%lf",&Man[i]);
		for (  i = 0; i < n; ++i )
			scanf("%lf",&women[i]);

		sort(Man,Man+n);
		sort(women,women+n);

		memset(now,0,sizeof(now));
		memset(now1,0,sizeof(now1));

		int number1 = 0, number2 = 0;

		number1 = search1();

		number2 = search2();

		printf("Case #%d: %d %d\n",cas,number1,number2);
}
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	scanf("%d",&T);
	int i = 0;
	while (T-- ) work(++i);
	return 0;
}
