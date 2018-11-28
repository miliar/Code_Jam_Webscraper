#include<iostream>
#include<string>
#include<fstream>

using namespace std;

int main()
{
    fstream f1,f2;
    f1.open("input.in",ios::in);
    f2.open("output.txt",ios::out);
    int t,w=1;
    f1>>t;
    while(t--)
    {
        int i,j,k,l,m,n,p,q,a[10][10],b[10][10],co=0;
        f1>>p;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
                f1>>a[i][j];
        }
        f1>>q;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                f1>>b[i][j];
            }
        }
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(a[p][i]==b[q][j])
                {
                    co++;
                    m=a[p][i];
                }
            }
        }
        if(co==0)
        {
            f2<<"Case #"<<w<<": Volunteer cheated!\n";
        }
        else if(co==1)
        {
            f2<<"Case #"<<w<<": "<<m<<"\n";
        }
        else
        {
            f2<<"Case #"<<w<<": Bad magician!\n";
        }
        w++;
    }
    return 0;
}
