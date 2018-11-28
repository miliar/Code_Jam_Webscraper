#include <iostream>
#include <fstream>

using namespace std;

fstream f("magic.in",ios::in);
fstream g("magic.txt",ios::out);

int grid[5][5],n,i,j,ans,q,p[17],t,m;



int main()
{
    f>>t;
    n=1;
    while(t>0)
    {g<<"Case #"<<n<<": ";

        for(i=1;i<=16;i++)
        p[i]=0;

        f>>q;
        for(i=1;i<=4;i++)
          for(j=1;j<=4;j++)
            f>>grid[i][j];

        for(i=1;i<=4;i++)
           p[grid[q][i]]=1;

        f>>q;

        for(i=1;i<=4;i++)
          for(j=1;j<=4;j++)
            f>>grid[i][j];
        m=0;
        for(i=1;i<=4;i++){
           if(p[grid[q][i]]==1)
           {ans=grid[q][i];
           m++;
           }
        }


        if(m==0)
        g<<"Volunteer cheated!\n";
        else
        if(m>1)
        g<<"Bad magician!\n";
        else
        g<<ans<<endl;
        t--;
        n++;

    }






    return 0;
}
