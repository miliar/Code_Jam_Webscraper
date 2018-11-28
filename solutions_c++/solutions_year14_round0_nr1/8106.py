#include <iostream>
#include <fstream>
#define ld long long int
using namespace std;
int main()
{
    ifstream romeo;
    ofstream rumon;
    romeo.open("A-small-attempt1.in");
    rumon.open("A-small-attempt1.out");
    ld tc, i, j, k, a1, a2, m1[4][4], m2[4][4], c, co;
    romeo>>tc;
    for(c=1;c<=tc;c++)
    {
        co=0;
        romeo>>a1;
        a1--;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                romeo>>m1[i][j];
        romeo>>a2;
        a2--;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                romeo>>m2[i][j];
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                if(m1[a1][i]==m2[a2][j])
                {
                    co++;
                    k=m1[a1][i];
                }
        if(co==0)
            rumon<<"Case #"<<c<<": Volunteer cheated!"<<endl;
        else if(co==1)
            rumon<<"Case #"<<c<<": "<<k<<endl;
        else if(co>1)
            rumon<<"Case #"<<c<<": Bad magician!"<<endl;
    }
}
