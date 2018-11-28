#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    fstream fin, fout;
    int test,ans1,ans2,i,j,x,k=0;

    fin.open("input.txt",ios::in);
    fout.open("output.txt",ios::out);

    fin>>test;

    int a[4][4];

    while(k++ < test)
    {
        int b[18]={0};

        fin>>ans1;

        for(i=0;i<=3;i++)
        for(j=0;j<=3;j++)
        fin>>a[i][j];


        for(i=0;i<=3;i++)
        {
            x=a[ans1-1][i];

            b[x]++;
        }


        fin>>ans1;


        for(i=0;i<=3;i++)
        for(j=0;j<=3;j++)
        fin>>a[i][j];



         for(i=0;i<=3;i++)
        {
            x=a[ans1-1][i];

            b[x]++;
        }

        x=0;

        ans1=0;
        for(i=0;i<=16;i++)
        {
            if(b[i]==2)
            {x++;
             ans1=i;
            }
        }

        fout<<"Case #"<<k<<": ";

        if(x==1)
        fout<<ans1<<endl;

        if(x>=2)
        fout<<"Bad magician!\n";

        if(x==0)
        fout<<"Volunteer cheated!\n";


    }

    return 0;
}
