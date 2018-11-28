#include <cstdio>
#include <algorithm>
using namespace std;

int v[20000];

int main()
{
    int T;
    scanf("%d", &T);
    for(int tn = 1; tn <= T; tn++)
    {
	int E, R, N;
	scanf("%d%d%d", &E, &R, &N);

	for(int i = 0; i < N; i++)
	    scanf("%d", v + i);

	long long int ans = 0;
	for(int i = 0, e = E; i < N; i++, e = min(E, e + R))
	{
	    bool flag = false;
	    for(int j = i + 1; j < N; j++)
		if(v[j] > v[i])
		{
		    int l = max(0ll, E - (j - i) * (long long)R);
		    if(l < e)
		    {			
			ans += (e - l) * (long long)v[i];
			e = l;
		    }
		    flag = true;
		    break;
		}
	    if(!flag)
	    {
		ans += e * (long long)v[i];
		e = 0;
	    }
	}
	


	printf("Case #%d: %I64d\n", tn, ans);

    }
    return 0;
}
