#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int main()
{
    int count = 0;
    int t;

    int data[100][100];
    int map[100][100];
    freopen("data.txt","r",stdin);
    freopen("ans.txt","w",stdout);
    scanf("%d",&t);
    while (t--)
    {
        count ++;
        int n,m;
        scanf("%d %d",&n,&m);
        memset(data,0,sizeof(data));
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
                scanf("%d",&data[i][j]);
        }
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                map[i][j] = 100;
        bool flag = false;

        while (!flag)
        {
            int max = 0;
            int maxi,maxj;
            bool finishcheck = true;
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                {
                    if (map[i][j] != data[i][j]) finishcheck = false;
                }
            if (finishcheck)
            {
                flag = true;
                printf("Case #%d: YES\n",count);
                break;
            }
            for (int i = 0; i < n; i++)
                for (int j = 0; j < m; j++)
                    if (map[i][j] != data[i][j] && data[i][j] > max)
                    {
                        maxi = i;
                        maxj = j;
                        max = data[i][j];
                    }
            bool avail = true;
            for (int i = 0; i < n; i++)
                if (data[i][maxj] > data[maxi][maxj])
                {
                    avail = false;
                    break;
                }
            if (avail)
            {
                for (int i = 0; i < n; i++)
                   map[i][maxj] = data[maxi][maxj];
                continue;
            }
            avail = true;
            for (int i = 0; i< m; i++)
                if (data[maxi][i] > data[maxi][maxj])
                {
                    avail = false;
                    break;
                }
            if (avail)
            {
                for (int i = 0; i < m; i++)
                    map[maxi][i] = data[maxi][maxj];
                continue;
            }
            flag = true;
            printf("Case #%d: NO\n",count);
            break;
        }
    }
}
