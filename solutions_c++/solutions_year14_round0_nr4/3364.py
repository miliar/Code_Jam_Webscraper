#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
    int t, count = 0, num, max, min;
    double *n, *k;
    scanf("%d",&t);
    while(t--)
    {
        count++;
        max = 0;
        min = 0;
        scanf("%d",&num);
        n = new double[num];
        k = new double[num];
        for(int i = 0; i<num ; ++i)
            scanf("%lf",&n[i]);
        for(int i = 0; i<num ; ++i)
            scanf("%lf",&k[i]);
        sort(n,n+num);
        sort(k,k+num);
        for(int p = num-1, q = num - 1; p >= 0; --p)
        {
            if(n[p] > k[q])
                min++;
            else
                q = q--;
        }
        for(int j = num-1 ; j>=0 ; --j)
        {
                if(n[j] < k[j])
                {
                    if(j!=0)
                    {
                        for(int k = 0; k<num ; ++k)
                            n[k] = n[k+1];
                    }
                }
                else
                    max++;
        }
        printf("Case #%d: %d %d\n",count,max,min);
    }
}
