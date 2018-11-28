#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
using namespace std;

int main()
{
    freopen("d_small.in","r",stdin);
    freopen("d_small.txt","w",stdout);
    int times,t;
    scanf("%d",&times);
    for (t = 0; t < times; t++)
    {
        int n;
        scanf("%d",&n);
        double dataa[1000];
        double datab[1000];
        for (int i = 0; i < n; i++)
            scanf("%lf",&dataa[i]);
        sort(dataa,dataa+n);
        for (int i = 0; i < n; i++)
            scanf("%lf",&datab[i]);
        sort(datab,datab+n);
        bool used[1000];
        memset(used,false,sizeof(used));
        int answerbefore = 0;
        for (int i = 0; i < n; i++)
        {
            bool flag = false;
            for (int j = 0; j < n; j++)
            {
                if (datab[j] > dataa[i] && !used[j])
                {
                    used[j] = true;
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                answerbefore = n - i;
                break;
            }
        }
        int answerafter = 0;
        memset(used,false,sizeof(used));
        int wpointer = 0;
        for (int i = 0; i < n; i++)
        {
            if (datab[wpointer] < dataa[i]){
                answerafter ++;
                wpointer++;
            }
        }
        printf("Case #%d: %d %d\n",t+1,answerafter,answerbefore);
    }
}
