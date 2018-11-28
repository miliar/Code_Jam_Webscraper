#include <fstream>

using namespace std;

unsigned m[17];

int main()
{
    unsigned t,n,i,j,k,aux,cnt,val;
    ifstream f("input.in");
    ofstream g("output.out");
    f>>t;
    for(k=1;k<=t;k++)
    {
        f>>n;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++)
            {
                f>>aux;
                if(i==n)
                    m[aux]=k;

            }

        f>>n;
        cnt=0;
        for(i=1;i<=4;i++)
            for(j=1;j<=4;j++){
                f>>aux;
                if(i==n)
                    if(m[aux]==k){cnt++;val=aux;}
            }

        if(cnt==1)g<<"Case #"<<k<<": "<<val<<'\n';
        else if(cnt==0)g<<"Case #"<<k<<": Volunteer cheated!"<<'\n';
        else g<<"Case #"<<k<<": Bad magician!"<<'\n';
    }
    return 0;
}
