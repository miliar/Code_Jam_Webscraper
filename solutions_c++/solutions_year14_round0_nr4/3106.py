#include<stdio.h>
#include<stdlib.h>

int compare (const void * a, const void * b)
{
  if (*(double*)a > *(double*)b) return -1;
  else if (*(double*)a < *(double*)b) return 1;
  else return 0; 
}

void solve()
{
    int n;
    double block[2][1001];
    
    scanf("%d\n", &n);

    for(int p = 0; p < 2; p++)
    {
        for(int i = 0; i < n; i++)
            scanf("%lf", &block[p][i]);  
    
        qsort(&block[p], n, sizeof(double), compare);
    }

    int npt = 0, kpt = 0, score = 0;
    while(npt < n && kpt < n)
    {
        if(block[0][npt] > block[1][kpt])
        {
            score++;
            npt++;
            kpt++;
        }
        else
            kpt++;
    }
    printf("%d ", score);

    npt = 0, kpt = 0, score = 0;
    while(npt < n && kpt < n)
    {
        if(block[1][kpt] > block[0][npt])
        {
            score++;
            npt++;
            kpt++;
        }
        else
            npt++;
    }
    printf("%d\n", n-score);
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("data.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif

    int T;
    
    scanf("%d", &T);
    for(int i = 1; i <= T; i++)
    {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;  
}
