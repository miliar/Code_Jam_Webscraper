#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int closed[10000100];

bool pal(register long long int x)
{
register char s[20] = {0};
sprintf(s, "%lld", x);
for(register int i = 0, j = strlen(s) - 1; i < j; i++, j--)
	if(s[i] != s[j])
		return false;
return true;
}
int
main(void)
{
long long int tmp1, tmp2;
register long long int a, i, b;
long long int T, test = 1;
scanf("%lld", &T);
while(T--)
	{
	long long int counter = 0;
	scanf("%lld %lld", &tmp1, &tmp2);
	a = tmp1;
	b = tmp2;
	for(i = ceil(sqrt(a)); i * i <= b; i++)
		if((closed[i] >= 0 && pal(i*i) && pal(i)))
			{
			closed[i] = 1;
			counter++;
			}
		else
			closed[i] = -1;
	printf("Case #%lld: %lld\n", test++, counter);
	}
return 0;
}


