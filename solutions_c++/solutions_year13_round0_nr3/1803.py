//Aleksander Łukasiewicz
#include<cstdio>
using namespace std;

typedef long long int LL;
const LL MAXN = 100000000000000ll;
const int MAXSIZE = 1000000;

int t, ind;
LL prep[MAXSIZE + 3];

bool is_palindrom(LL p)
{
    int number[20], len = 0;
    while(p)
	number[len++] = p%10, p/=10;
    for(int i=0, j=len-1; i<j; i++, j--)
	if(number[i]!=number[j])
	    return false;
    return true;
}

void preprocessing()
{
    for(LL i=1; i*i<=MAXN; i++)
	if(is_palindrom(i) && is_palindrom(i*i))
	    prep[ind++] = i*i;
}

int count(LL A, LL B)
{
    int res = 0;
    for(int i=0; i<ind; i++)
	if(A<=prep[i] && prep[i]<=B)
	    res++;
    return res;
}

int main()
{
    preprocessing();
    scanf("%d", &t);
    for(int i=1; i<=t; i++)
    {
	LL A, B;
	scanf("%lld %lld", &A, &B);
	printf("Case #%d: %d\n", i, count(A,B));
    }

return 0;
}