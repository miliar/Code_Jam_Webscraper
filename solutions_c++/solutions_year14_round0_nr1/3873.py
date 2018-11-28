#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int n,c1,c2;
    int temp;
    int a[4][4],b[4][4];

    fin>>n;
    for(int i=1;i<=n;i++)
    {
        fin>>c1;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                fin>>a[j][k];
            }
        }
        fin>>c2;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                fin>>b[j][k];
            }
        }
        c1--;
        c2--;
        int count=0;
        temp=0;
        int num;
        for(int j=0;j<4;j++)
        {
            num=a[c1][j];
            for(int k=0;k<4;k++)
            {
                if(num==b[c2][k])
                {
                    count++;
                    temp=b[c2][k];
                }
            }
        }
        if(count==0)
        {
            fout<<"Case #"<<i<<": "<<"Volunteer cheated!\n";
        }
        else if(count==1)
        {
            fout<<"Case #"<<i<<": "<<temp<<"\n";
        }
        else
        {
            fout<<"Case #"<<i<<": "<<"Bad magician!\n";
        }
    }
    return 0;
}
