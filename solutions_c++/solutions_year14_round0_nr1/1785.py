#include <iostream>
#include <stdio.h>

#include <fstream>


using namespace std;

int main()
{
    ifstream in("A-small-attempt8.in");
    ofstream out("new.out");
int aux,j,h,t,respuesta,mat[5][3],i,repe,carta;

in>>t;
for(i=1;i<=t;i++)
{
    in>>respuesta;
    for(h=1;h<=4;h++)
    {
        if(h==respuesta)
        {
            for(j=1;j<=4;j++)
            {
                in>>mat[j][1];
            }
        }
        else
        {
            for(j=1;j<=4;j++)
            {

                in>>aux;
            }
        }
    }
    in>>respuesta;
    for(h=1;h<=4;h++)
    {
        if(h==respuesta)
        {
            for(j=1;j<=4;j++)
            {
                in>>mat[j][2];
            }
        }
        else
        {
            for(j=1;j<=4;j++)
            {

                in>>aux;
            }
        }
    }
    out<<"Case #"<<i<<": ";
    repe=0;

    for(h=1;h<=4;h++)
    {
    for(j=1;j<=4;j++)
    {
        if(mat[h][1]==mat[j][2])
        {
            if(repe==0)
            {
                repe=1;
                carta=mat[j][2];
            }
            else
            {
                repe=2;
            }
        }
    }

    }

    if(repe==0)
    {
        out<<"Volunteer cheated!"<<endl;
    }
    else
    {
        if(repe==1)
        {
            out<<carta<<endl;
        }
        else
        {
            out<<"Bad magician!"<<endl;
        }
    }

}

in.close();
out.close();


return 0;
}
