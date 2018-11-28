#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int tab[4][4];
bool first[17],second[17];
int main()
{
    vector<int> solves;
    int a,b,t,z;
    scanf("%d",&z);
    t=0;
    while(t<z)
    {
        t++;
        solves.resize(0);
        for(int i=0; i<17; i++)
        {
            first[i]=false;
            second[i]=false;
        }

        scanf("%d",&a);
        a--;

        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
            {
                scanf("%d",&tab[i][j]);
                if(i==a)
                    first[tab[i][j]]=true;
            }

        scanf("%d",&b);
        b--;

        for(int i=0; i<4; i++)
            for(int j=0; j<4; j++)
            {
                scanf("%d",&tab[i][j]);
                if(i==b)
                    second[tab[i][j]]=true;
            }

        for(int i=1;i<=16;i++)
        if(first[i] && second[i])
        solves.push_back(i);

        printf("Case #%d: ",t);
        if(solves.size()==1)
        printf("%d\n",solves[0]);
        else if(solves.size()==0)
        printf("Volunteer cheated!\n");
        else  printf("Bad magician!\n");
    }


    return 0;

}
