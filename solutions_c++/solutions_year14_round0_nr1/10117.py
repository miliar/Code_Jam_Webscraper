#include <cstdio>
#include <set>

using namespace std;

int main()
{
    int tests;
    scanf("%d", &tests);
    for(int dupa=1; dupa<=tests; dupa++)
    {
        int rowa,rowb;
        scanf("%d", &rowa);
        int c1,c2,c3,c4, temp;
        int d1,d2,d3,d4;
        for(int i=1;i<=rowa; i++)
        {
            scanf("%d %d %d %d", &c1,&c2,&c3,&c4);
        }
        for(int i=rowa+1; i<=4; i++)
            for(int j=0;j<4;j++)
                scanf("%d", &temp);
        scanf("%d", &rowb);


        for(int i=1;i<=rowb; i++)
        {
            scanf("%d %d %d %d", &d1,&d2,&d3,&d4);
        }

        for(int i=rowb+1; i<=4; i++)
            for(int j=0;j<4;j++)
                scanf("%d", &temp);

        set<int> test;
        test.insert(d1);
        test.insert(d4);
        test.insert(d3);
        test.insert(d2);
        int times=0;
        int num=-1;
        if(test.find(c1)!=test.end())
        {
            num=c1;
            times++;
        }
        if(test.find(c2)!=test.end())
        {
            num=c2;
            times++;
        }
        if(test.find(c3)!=test.end())
        {
            num=c3;
            times++;
        }
        if(test.find(c4)!=test.end())
        {
            num=c4;
            times++;
        }
        printf("Case #%d: ", dupa);
        if(times>1)
            printf("Bad magician!\n");
        if(times==1)
            printf("%d\n", num);
        if(times==0)
            printf("Volunteer cheated!\n");
    }
}

