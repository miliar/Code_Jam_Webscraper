#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;
int map[5][5];
vector<int> vec;
int main()
{
    freopen("dd.in","r",stdin);
    freopen("out.txt","w+",stdout);
    int ncase,T=0;
    scanf("%d",&ncase);
    while(ncase--)
    {
        printf("Case #%d: ",++T);
        int n=4;
        vec.clear();
        int row;
        scanf("%d",&row);
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
            scanf("%d",&map[i][j]);
        }
        for(int i=1;i<=4;i++)
        vec.push_back(map[row][i]);
        scanf("%d",&row);
        for(int i=1;i<=n;i++)
        {
            for(int j=1;j<=n;j++)
            scanf("%d",&map[i][j]);
        }
        int num=0,po=0;
        for(int i=0;i<4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                if(vec[i]==map[row][j])
                {
                    po=vec[i];
                    num++;
                    break;
                }
            }
        }
        if(num==1)
        printf("%d\n",po);
        else if(num>1)
        printf("Bad magician!\n");
        else
        printf("Volunteer cheated!\n");
    }
    return 0;
}
