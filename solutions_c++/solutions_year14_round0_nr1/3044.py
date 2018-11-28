#include<fstream>
using namespace std;
int main()
{
    fstream f,g;
    f.open("magic.in",ios::in);
    g.open("magic.out",ios::out);
    int R[3],v[17]={0},A[17][17],i,j,p,nr,T,k;
    f>>T;
    for(k=1; k<=T; k++)
    {
        nr=0;
        for(i=1; i<=16; i++)
            v[i]=0;
        g<<"Case #"<<k<<": ";
        for(i=1; i<=2; i++)
        {
            f>>R[i];
            for(j=1; j<=4; j++)
                for(p=1; p<=4; p++)
                {
                    f>>A[j][p];
                    if(j==R[i])
                        v[A[j][p]]++;
                }
        }
        for(i=1; i<=16; i++)
            if(v[i]==2)
            {
                nr++;
                p=i;
            }
        if(nr==1)
            g<<p<<'\n';
        if(nr>1)
            g<<"Bad magician!"<<'\n';
        if(nr==0)
            g<<"Volunteer cheated!"<<'\n';

    }
}
