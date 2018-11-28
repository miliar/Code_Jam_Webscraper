#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

int device[1111111];
ll psum[1111111];
ll que[1111111];

int main(void)
{
	int T = 0;
	int TK = 0;
	scanf("%d",&T);
	while(T--)
	{
		printf("Case #%d: ",++TK);
		int N = 0;
		scanf("%d",&N);
		int p,q,r,s;
		scanf("%d %d %d %d",&p,&q,&r,&s);
		for(int i = 0;i < N;i++) device[i] = ((ll)i*p+q) % r + s;
		psum[0] = device[0];
		for(int i = 1;i < N;i++) psum[i] = psum[i-1] + device[i];
		for(int i = 0;i < N;i++) que[i] = psum[i];

		ll ans = 0;
		int where = 0;
		for(int i = 0;i < N;i++)
		{
			ll todo = psum[N-1] + (i ? psum[i-1] : 0); // todo +
			// max for every j > i
			// min(todo - psum[j], psum[j])
			while(where < N && todo >= 2*psum[where]) where++;
			ll tans = todo-psum[where];
			if(where) tans = max(tans,psum[where-1]);
			if(i) tans = min(tans, psum[N-1] - psum[i-1]); // upper bound
			ans = max(ans, tans);
		}
		printf("%.10f\n",ans/(double)psum[N-1]);
	}
	while(getchar() != EOF);
	return 0;
}
