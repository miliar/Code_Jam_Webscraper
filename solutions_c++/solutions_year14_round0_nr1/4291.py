#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    std::ifstream myfile("A-small-attempt0.in");
    std::ofstream myfile2("output.txt");
    int t;
    myfile>> t;
    for(int i=0;i<t;i++)
    {
        int a[4][4];
        int b[4][4];
        int r1,r2;
        int card,flag=0;
        myfile>> r1;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                myfile>>a[j][k];
            }
        }
        myfile>>r2;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                myfile>>b[j][k];
            }
        }
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                if(a[r1-1][j]==b[r2-1][k])
                {
                    flag+=1;
                    card= a[r1-1][j];
                }
            }
        }
        if(flag>1)
        {
            myfile2<<"Case #"<<(i+1)<<": Bad magician!\n";
        }
        else if(flag==0)
        {
            myfile2<<"Case #"<<(i+1)<<": Volunteer cheated!\n";
        }
        else
        {
            myfile2<<"Case #"<<(i+1)<<": "<<card<<'\n';
        }
    }
    myfile.close();
    myfile2.close();
    return 0;
}
