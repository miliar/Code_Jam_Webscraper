#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    fstream input("input.in",ios::in);
    fstream output("output.out",ios::out);
    int t;
    input>>t;
    int mata[4][4];
    int matb[4][4];
    int n1,n2;
    int j,k,c=0,num=0;
    for(int i=0;i<t;++i)
    {
        input>>n1;
        for(j=0;j<4;++j)
        {
            for(k=0;k<4;++k)
            {
                input>>mata[j][k];
            }
        }
        input>>n2;
        for(j=0;j<4;++j)
        {
            for(k=0;k<4;++k)
            {
                input>>matb[j][k];
            }
        }
        output<<"Case #"<<i+1<<": ";
        for(j=0;j<4;++j)
            for(k=0;k<4;++k)
                if(mata[n1-1][j]==matb[n2-1][k])
                {
                    c++;
                    num=mata[n1-1][j];
                }
        if(c==0)
            output<<"Volunteer cheated!\n";
        else if(c==1)
            output<<num<<"\n";
        else
            output<<"Bad magician!\n";
            c=0;
    }
    return 0;
}
