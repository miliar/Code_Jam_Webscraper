#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <set>
using namespace std;

int val[10][5];

int main()
{
    //freopen("input.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    int i,j,k;
    int T;
    scanf("%d",&T);
    int test=0;
    while(T--)
    {
        int x,y;
        scanf("%d",&x);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&val[i][j]);
                //cout<<val[i][j]<<".."<<endl;
            }
        }
        scanf("%d",&y);
        for(;i<8;i++)
        {
            for(j=0;j<4;j++)
            {
                scanf("%d",&val[i][j]);
            }
        }
        x--,y--;
        y+=4;

        set<int> s;
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                if(val[x][j]==val[y][k])
                {
                    s.insert(val[x][j]);
                }
            }
        }
        printf("Case #%d: ",++test);
        if(s.size()==1)
        {
            printf("%d\n",*s.begin());
        }
        else if(s.size()>1)
        {
            printf("Bad magician!\n");
        }
        else
        {
            printf("Volunteer cheated!\n");
        }
    }
    return 0;
}
