#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

ifstream F("p.in");
ofstream G("p.out");

int t,row[2],a[2][6][6];
int co[20];

int main()
{
    F>>t;
    for (int ts=1;ts<=t;++ts)
    {
        memset(co,0,sizeof(co));
        for (int k=0;k<2;++k)
        {
            F>>row[k];
            for (int i=0;i<4;++i)
                for (int j=0;j<4;++j)
                    F>>a[k][i][j];
        }
        for (int k=0;k<2;++k)
            for (int j=0;j<4;++j)
                co[ a[k][row[k]-1][j] ]++;
        int ans = 0 , val = 0;
        for (int i=1;i<=16;++i)
            if ( co[i] > 1 )
            {
                ans++;
                val = i;
            }
        G<<"Case #"<<ts<<": ";
        if ( ans == 1 )
        {
            G<<val<<'\n';
        } else
        if ( ans == 0 )
        {
            G<<"Volunteer cheated!\n";
        } else
        G<<"Bad magician!\n";
    }
}
