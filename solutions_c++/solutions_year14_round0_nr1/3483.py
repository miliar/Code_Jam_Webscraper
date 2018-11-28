#include <fstream>

using namespace std;

ifstream f("prob1.in");
ofstream g("prob1.out");

int a[5],b[5],t,i,j,k,p,q,aux,val,contor;

int main()
{
    f>>t;

    for(i=1;i<=t;i++)
    {
        contor=0;
        f>>k;
        for(p=1;p<=4;p++)
            for(q=1;q<=4;q++)
            {
                f>>aux;
                if (p==k) a[q]=aux;
            }

        f>>k;
        for(p=1;p<=4;p++)
            for(q=1;q<=4;q++)
            {
                f>>aux;
                if (p==k) b[q]=aux;
            }


        for(p=1;p<=4;p++)
            for(q=1;q<=4;q++)
                if (a[p]==b[q])
                {
                    contor++;
                    val=a[p];
                }

        g<<"Case #"<<i<<": ";
        if (contor>1) g<<"Bad magician!";
        else if (contor==1) g<<val;
        else g<<"Volunteer cheated!";
        g<<"\n";
    }


    return 0;
}
