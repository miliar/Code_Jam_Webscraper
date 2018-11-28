#include <cstdio>
#include <algorithm>
using namespace std;

int bitc(long long int n)
{
    int ret = 0;
    while(n)
	ret++, n &= n - 1;
    return ret;
}

long long int f(int N, long long int P)
{
	long long int pp = P;
	while(pp & (pp - 1))
	    pp &= pp - 1;

	int nn = N;
	int alc = 0;
	while((1ll << (nn - alc)) > pp)
	    alc++;

        return (1ll << N) - (1ll << alc);
}

long long int f2(int N, long long int P)
{
	long long int pp = (1ll << N) - P;
	if(pp == 0)
	    return (1ll << N) - 1;

	while(pp & (pp - 1))
	    pp &= pp - 1;

	int nn = N;
	int alc = 0;
	while((1ll << (nn - alc)) > pp)
	    alc++;

        return (1ll << alc) - 2;   
}



int main()
{
    int T;
    scanf("%d", &T);
    for(int tn = 1; tn <= T; tn++)
    {
	printf("Case #%d: ", tn);

	int N;
	long long int P;
	scanf("%d%I64d", &N, &P);
	long long ans1 = 0, ans2 = 0;

	ans1 = f2(N, P);
	ans2 = f(N, P);


	printf("%I64d %I64d\n", ans1, ans2);
    }
    return 0;
}
