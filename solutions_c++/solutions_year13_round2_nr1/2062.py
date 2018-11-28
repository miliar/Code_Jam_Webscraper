#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>

using namespace std ;
	int cas_n, c;
	int A, N;
	int mote[1000010];
	int ans, first, cnt;
int main()
{

    freopen("input.txt","r",stdin);
   // freopen("output.txt","w",stdout);

    scanf("%d", &c);
    for(int c = 1 ; c <= cas_n ; c++)
    {

 		scanf("%d%d", &A, &N);
		for(int i=0; i<N; ++i) scanf("%d", &mote[i]);
/*
		sort(mote, mote+N);

		ans = 0;
		cnt = 0;
		first = 0;

		for(int i=0; i<N; ++i)
        {
			while( A <= mote[i] )
            {
				if( ans <= 0 ) first = i;

                A += A - 1;
                cnt++;
                if( cnt >= N - i ) break;
            }

			ans += cnt;
			cnt = 0;

			if( ans >= N - first )
                {
				ans = N - first;
				goto END_FLAG;
			}

			A += mote[i];
		}
*/
      //  END_FLAG:
		printf("Case #%d: %d\n", c, ans);


    }


    return 0 ;
}

