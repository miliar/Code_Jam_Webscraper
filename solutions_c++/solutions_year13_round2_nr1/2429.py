#include<stdio.h>
#include<stdlib.h>
 
int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int cases, n, mote[101] = {0}, m, step[101]={0}, cur[101] = {0}, tmps, tmpm;

int get_moves(int x, int y)
{
    int ret = 0;
    
    for(int i = x; i <= y; i++)
    {
        while(tmpm <= mote[i])
        {
            tmpm += (tmpm - 1);
            ret++;
        }
        tmpm += mote[i];
    }

    return ret;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif


    scanf("%d", &cases);

    for(int i = 1; i <= cases; i++)
    {
        scanf("%d %d", &m, &n);
        for(int j = 1; j <= n; j++)
            scanf("%d", &mote[j]);
        qsort(mote, n+1, sizeof(int), compare);

        printf("Case #%d: ", i);
        if(m == 1 || m == 0) printf("%d\n", n);
        else
        {
            cur[0] = m;
            for(int j = 1; j <= n; j++)
            {
                if(cur[j-1] > mote[j])
                {
                    cur[j] = cur[j-1] + mote[j];
                    step[j] = step[j-1];
                }
                else
                {
                    cur[j] = cur[j-1];
                    step[j] = step[j-1] + 1;

                    tmpm = cur[j-step[j]];
                    tmps = get_moves(j-step[j]+1, j);
                
                    if(step[j-step[j]] + tmps < step[j])
                    {
                        cur[j] = tmpm;
                        step[j] = step[j-step[j]] + tmps;
                    }
                }
            }
            printf("%d\n", step[n]);
        }
    }
	return 0;

}