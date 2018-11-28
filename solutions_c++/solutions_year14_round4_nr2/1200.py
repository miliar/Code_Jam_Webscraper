#include <cstdio>
#include <algorithm>
#include <cstring>
#include <map>
using namespace std;

const int MAXN = 1010;
int num[MAXN], rank[MAXN], finalN[MAXN], temp[MAXN];

int main()
{
    int TC, N;
    scanf("%d", &TC);

    for(int tc = 1; tc <= TC; ++tc)
    {
        scanf("%d", &N);
        for(int i = 0; i < N; i++)
        {
            scanf("%d", &num[i]);
            rank[i] = num[i];
        }

        map <int, int> rtn;
        sort(rank, rank+N);

        for(int i = 0; i < N; i++)
            rtn[ rank[i] ] = i;
        for(int i = 0; i < N; i++)
            num[i] = rtn[ num[i] ] ;

        int ans = 5566, idx = 0; //cannot die

        for(int a = 0; a < N; a++)
            if(num[a] == N-1)
            {
                idx = a;
                break;
            }
        
        int upper = 1<<(N-1);
        //enumerate pivot
        for(int i = 0; i < upper; i++)
        {
            //memcpy(finalN, num, sizeof(num));
            int center = 0, cnt[2] = {0, 0};
            for(int j = 0; j < N-1; j++)
                if( (i & (1<<j)) == 0 )
                    ++center;

            finalN[ center ] = N-1;
            for(int j = N-2; j >= 0; j--)
                if( (1<<j) & i )
                {
                    finalN[ center+1+cnt[1] ] = j;
                    cnt[1]++;
                }
                else
                {
                    finalN[ center-1-cnt[0] ] = j;
                    cnt[0]++;
                }
           /* if(idx > i)
            {
                for(int j = idx; j > i; j--)
                    swap(finalN[j], finalN[j-1]);
            }
            else if(idx < i)
            {
                for(int j = idx; j < i; j++)
                    swap(finalN[j], finalN[j+1]);
            }
            if(i != 0) sort(finalN, finalN+i);

            if(i+1 < N)
            {
                sort(finalN+i+1, finalN+N);
                reverse(finalN+i+1, finalN+N); 
            }*/

            //for(int a = 0; a < N; a++)
            //    printf("%d ", finalN[a]);
            //printf("\n");            
            int inv = 0;
            map <int, int> invN;
            memcpy(temp, num, sizeof(num));
            for(int j = 0; j < N; j++)
                invN[ finalN[j] ] = j;
            for(int j = 0; j < N; j++)
                temp[ j ] = invN[ temp[j] ];

            for(int a = 0; a < N; a++)
                for(int b = a+1; b < N; b++)
                    if( temp[a] > temp[b] )
                        ++inv;
            
            //printf("OH ? %d - %d\n", i, inv);
            ans = min(ans, inv);         
        }

        printf("Case #%d: %d\n", tc, ans);
    }

    return 0;
}
