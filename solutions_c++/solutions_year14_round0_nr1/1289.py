#include<cstdio>
#include<iostream>
#include<set>
using namespace std;
int main()
{
    int ti;scanf("%d",&ti);
    for(int ca=1; ca<=ti; ca++)
    {
        set<int>list;
        int row;scanf("%d",&row);row --;
        for(int i = 0; i < 4; i ++)
        for(int j = 0; j < 4; j ++)
        {
            int tmp;scanf("%d",&tmp);
            if(i == row)
            {
                list.insert(tmp);
            }
        }
        int cnt = 0, w = -1;
        scanf("%d",&row);row --;
        for(int i = 0; i < 4; i ++)
        for(int j = 0; j < 4; j ++)
        {
            int tmp;scanf("%d",&tmp);
            if(i == row && list.find(tmp) != list.end())
            {
                cnt ++;
                w = tmp;
            }
        }
        printf("Case #%d: ",ca);
        if(cnt > 1)printf("Bad magician!\n");
        else if(cnt == 0)printf("Volunteer cheated!\n");
        else printf("%d\n",w);
    }
}
