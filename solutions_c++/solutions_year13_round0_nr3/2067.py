#include<cstdio>
#include<cmath>
using namespace std;
char tab[15];
int pref[10000002];
bool palindrom(long long a)
{
	int i, j;
	for (i=0; a; i++)
	{
		tab[i] = a%10;
		a/=10;
	}
	for (i--, j=0; j<i; j++, i--)
		if(tab[i]!=tab[j]) return 0;
	return 1;
}

int main()
{
int t, res;
scanf("%d", &t);

pref[0] = 1;
for (long long i=1; i<=10000000; i++)
	pref[i] = ( (palindrom(i) && palindrom(i*i) )? pref[i-1] + 1 : pref[i-1]);
	
for (int k=1; k<=t; k++)
{
	long long a, b;
	scanf("%lld%lld", &a, &b);
	long long A = sqrt((long double)a), B = sqrt((long double) b)+1;
	if(A*A < a) A++;
	if(A*A < a) A++;
	if(B*B > b) B--;
	if(B*B > b) B--;
	
	int wynik = pref[B] - pref[A-1];
	printf("Case #%d: %d\n", k, wynik);
}
return 0;
}
