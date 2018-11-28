#include <fstream>

using namespace std;

int a[4][4],T;

int main()
{
    char q;
    int o,x,al=0,j,k,cont;
    ifstream f1("A-large.in");
    ofstream f2("A-large.out");
    f1>>T;
    for(int i=0;i<T;i++)
    {
        al=0;
        if(i)
            f2<<'\n';
        f2<<"Case #"<<i+1<<": ";
        for(j=0;j<4;j++)
            for(k=0;k<4;k++)
            {
                f1>>q;
                if(q=='X')
                    a[j][k]=1;
                else if(q=='O')
                    a[j][k]=2;
                else if(q=='.')
                {
                    a[j][k]=0;
                    al=1;
                }
                else if(q=='T')
                    a[j][k]=3;
            }

        o=0;
        x=0;
        cont=0;
        for(j=0;j<4;j++) // Diagonala principala
            if(a[j][j]==1)
                x++;
            else if(a[j][j]==2)
                o++;
            else if(a[j][j]==3)
            {
                x++;
                o++;
            }
        if(x==4)
        {
            f2<<"X won";
            cont=1;
            continue;
        } else if (o==4)
        {
            f2<<"O won";
            cont=1;
            continue;
        }
        o=0;
        x=0;
        for(j=0;j<4&&!cont;j++) // Diagonala secundara
            if(a[j][3-j]==1)
                x++;
            else if(a[j][3-j]==2)
                o++;
            else if(a[j][3-j]==3)
            {
                x++;
                o++;
            }
        if(x==4)
        {
            f2<<"X won";
            continue;
        } else if (o==4)
        {
            f2<<"O won";
            continue;
        }
        for(j=0;j<4&&!cont;j++) // Fiecare linie
        {
            o=0;
            x=0;
            for(k=0;k<4;k++) // Coloane...
                if(a[j][k]==1)
                    x++;
                else if(a[j][k]==2)
                    o++;
                else if(a[j][k]==3)
                {
                    x++;
                    o++;
                }
            if(x==4)
            {
                f2<<"X won";
                cont=1;
                break;
            } else if (o==4)
            {
                f2<<"O won";
                cont=1;
                break;
            }
        }
        if(!cont)
        {
            for(j=0;j<4&&!cont;j++) // Fiecare coloana
            {
                o=0;
                x=0;
                for(k=0;k<4;k++) // Linie...
                    if(a[k][j]==1)
                        x++;
                    else if(a[k][j]==2)
                        o++;
                    else if(a[k][j]==3)
                    {
                        x++;
                        o++;
                    }
                if(x==4)
                {
                    f2<<"X won";
                    cont=1;
                    break;
                } else if (o==4)
                {
                    f2<<"O won";
                    cont=1;
                    break;
                }
            }
            if(!cont)
            {
                if(al)
                    f2<<"Game has not completed";
                else
                    f2<<"Draw";
            }
        }
    }
    return 0;
}
