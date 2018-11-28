#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;

int main()
{
	int cas_n, cas;
	int A, N;
	int mote[1000010];
	int ans, first, count;

	scanf("%d", &cas_n);
	for(cas=1; cas<=cas_n; cas++) {
		scanf("%d %d", &A, &N);
		for(int i=0; i<N; ++i)
			scanf("%d", &mote[i]);
		sort(mote, mote+N);
		ans = 0;
		count = 0;
		first = 0;
		for(int i=0; i<N; ++i) {
			while( A <= mote[i] ) {
				if( ans <= 0 )
					first = i;
				A += A - 1;
				count++;
				if( count >= N - i )
					break;
			}
			ans += count;
			count = 0;
			if( ans >= N - first ) {
				ans = N - first;
				goto end;
			}
			A += mote[i];
		}
end:
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
