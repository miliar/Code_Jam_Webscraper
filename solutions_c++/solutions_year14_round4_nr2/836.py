#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int ans;
int data[1050];
int swap(int x,int y)
{
    int temp;
    temp = data[x];
    data[x] = data[y];
    data[y] = temp;
    ans ++;
}
int main()
{
    int times;
    freopen("B-large (1).in","r",stdin);
    freopen("B-large.out","w",stdout);
    cin>>times;
    for (int t = 0; t < times; t++)
    {
        int n;

        scanf("%d",&n);
        memset(data,0,sizeof(data));
        for (int i = 0; i < n; i++)
        {
             scanf("%d",&data[i]);
        }

        int p = 0;
        int pp = n-1;
        ans = 0;
        for (int i = 0; i < n; i++)
        {
            int min = 2147000000;
            int minx = -1;
            for (int j = p; j <= pp; j++)
            {
                if (data[j] < min)
                {
                    min = data[j];
                    minx = j;
                }
            }
            if (pp - minx < minx - p)
            {
                for (int j = minx; j < pp; j++)
                {
                    swap(j,j+1);
                }
                pp --;

            }
            else
            {
                for (int j = minx; j > p; j--)
                {
                    swap(j,j-1);
                }
                p ++ ;
            }
        }
        printf("Case #%d: %d\n",t+1, ans);
    }
}
