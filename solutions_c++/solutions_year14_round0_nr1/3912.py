#include <fstream>
using namespace std;

ifstream f("magictrick.in");
ofstream g("magictrick.out");

int ap[17],t,q1,q2;

int main()
{
    int i,j,cod,x;
    f>>t;
    for(i=1;i<=t;i++){
        for(j=1;j<=16;j++)
            ap[j]=0;
        cod=0;
        f>>q1;
        for(j=1;j<=4*(q1-1);j++)
            f>>x;
        for(j=4*(q1-1)+1;j<=4*q1;j++){
            f>>x;
            ap[x]++;
        }
        for(j=4*q1+1;j<=16;j++)
            f>>x;
        f>>q2;
        for(j=1;j<=4*(q2-1);j++)
            f>>x;
        for(j=4*(q2-1)+1;j<=4*q2;j++){
            f>>x;
            ap[x]++;
        }
        for(j=4*q2+1;j<=16;j++)
            f>>x;
        for(j=1;j<=16;j++)
            if(ap[j]==2){
                cod++;
                x=j;
            }
        g<<"Case #"<<i<<": ";
        if(cod==0)
            g<<"Volunteer cheated!";
        if(cod==1)
            g<<x;
        if(cod>1)
            g<<"Bad magician!";
        g<<"\n";
    }
    f.close();
    g.close();
    return 0;
}
