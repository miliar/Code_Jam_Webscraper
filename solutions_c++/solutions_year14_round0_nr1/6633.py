#include<iostream>
#include<fstream>
using namespace std;

int n,m,c;
int a[10000];

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    fin>>n;
    for (int k=1;k<=n;k++)
    {
        fin>>c>>m;
        for (int i=1;i<=m;i++) fin>>a[i];
        for (int i=1;i<=m;i++)
            for (int j=i+1;j<=m;j++)
             if (a[i]+a[j]==c)
                {
                    fout<<"Case #"<<k<<": "<<i<<" "<<j<<endl;
                    break;
                }

    }
    fin.close();
    fout.close();
}

