#include <fstream>
#include <bitset>
using namespace std;
bitset <20> R1,R2;
int t,a1,a2,x,i,j,k;
ifstream fin("cit.in");
ofstream fout("cit.out");
int main()
{
    fin>>t;
    for(k=1;k<=t;k++)
    {
        R1.reset();
        R2.reset();
        fin>>a1;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
            {
                fin>>x;
                if(i==a1)
                    R1[x]=1;
            }
        fin>>a2;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
            {
                fin>>x;
                if(i==a2)
                    R2[x]=1;
            }
        fout<<"Case #"<<k<<": ";
        if((R1&R2).count()==1)
        {
            for(i=1;i<=16;i++)
                if(R1[i]==1&&R2[i]==1)
                {
                    fout<<i<<'\n';
                    break;
                }
        }
        if((R1&R2).count()>1)
            fout<<"Bad magician!\n";
        if((R1&R2).count()==0)
            fout<<"Volunteer cheated!\n";

    }
    return 0;
}
