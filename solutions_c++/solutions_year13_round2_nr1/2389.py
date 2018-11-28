#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<iostream>

using namespace std;

int arr[105];

int calNeededMove(int a, int x, int tot)
{
    int ret = 0;
    while(1)
    {
        a = 2*a - 1;
        ret++;
        if(ret > tot)
            return 2*tot;
        if(x<a)
            break;
    }
    return ret;
}
int main(void)
{
    int T;
    freopen("A-small-attempt3.in","r", stdin);
    freopen("out.out","w", stdout);
    scanf("%d",&T);
    for(int t = 0; t<T; t++)
    {
        int a,n;
        scanf("%d%d",&a,&n);
        for(int i = 0; i<n; i++)
        {
            scanf("%d",&arr[i]);
        }

        sort(arr, arr + n);
        int res = 0;

        for(int i = 0; i<n; i++)
        {
            if(arr[i] < a)
            {
                a += arr[i];
            }
            else if(arr[i] < 2*a - 1)
            {
                a = 2*a - 1;
                a += arr[i];
                res++;
            }
            else
            {
                int x = calNeededMove(a,arr[i], n-i);
                if(x > (n-i-1))
                    res++;
                else
                {
                    for(int j = 0; j<x; j++)
                    {
                        a = 2*a - 1;
                        //printf("*%d ", a);
                        res++;
                    }
                    a += arr[i];
                }
            }

        }

        printf("Case #%d: %d\n",t + 1, res);
    }
    return 0;
}
