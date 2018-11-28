#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>

#define module 1000002013
using namespace std;
int n,m;


long long cost(int st,int ed, int p)
{
    int k = st - ed;
    return ((2*n-k+1)*k)/2*p;
}
int onboard[10000];
int boardlist[10000];
int slist[10000];
int pointon;
int st[10000],ed[10000],people[10000];
long long originalsum,bestsum;

int main()
{
    freopen("a.in","r",stdin);
    freopen("b.in","w",stdout);
    int times;
    scanf("%d",&times);
    for (int time = 0;time<times;time ++ )
    {
        scanf("%d%d",&n,&m);
        long long originalsum = 0;
        memset(onboard,0,sizeof(onboard));
        memset(boardlist,0,sizeof(boardlist));
        pointon = 0;
        memset(slist,0,sizeof(slist));
        originalsum = 0;
        bestsum = 0;
        for (int i = 0; i < m; i++)
        {
            scanf("%d%d%d",&st[i],&ed[i],&people[i]);
            originalsum = (originalsum + cost(st[i],ed[i],people[i])) % module;
            slist[i*2] = st[i];
            slist[i*2+1] = ed[i];
        }
        sort(slist,slist+2*m);
        for (int i = 0; i < 2*m; i++)
        {
            if (i != 0)
                while (slist[i-1] == slist[i]) i++;
            for (int j = 0; j < m; j++)
            {
                if (st[j] == slist[i])
                {onboard[pointon] = people[j];
                 boardlist[pointon++] = st[j];
                }
            }
            for (int j = 0; j < m; j++)
            {
                if (ed[j] == slist[i])
                {
                     int temp = people[j];
                     while (temp > 0)
                     {
                         if (onboard[pointon - 1] > temp)
                         {
                             onboard[pointon - 1] -= temp;
                             bestsum = (bestsum + cost(boardlist[pointon - 1],ed[j],temp)) % module;
                             temp = 0;
                         }
                         else
                         {
                             pointon --;
                             bestsum = (bestsum + cost(boardlist[pointon],ed[j],onboard[pointon])) % module;
                             temp -= onboard[pointon];
                             onboard[pointon] = 0;
                         }
                     }
                }

            }
        }
        printf("Case #%d: %d\n",time+1,(originalsum - bestsum + module)%module);
    }
}
