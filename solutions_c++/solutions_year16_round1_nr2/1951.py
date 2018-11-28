#include<iostream>
#include<fstream>
#include<string>
#include<cmath>
using namespace std;

int main()
{
    ifstream fin("B-large.in");
    ofstream fout("output.out");
    int t;
    fin>>t;
    for(int z=1;z<=t;z++)
    {
        int n,i,j;
        fin>>n;
        int a[n],c[2501];
        for(i=0;i<2501;i++)
            c[i]=0;
        for(j=0;j<2*n-1;j++)
        {
        for(i=0;i<n;i++)
          {
                fin>>a[i];
                c[a[i]]++;
          }
        }
        fout<<"Case #"<<z<<": ";
        for(i=0;i<2501;i++)
            {
                if(c[i]%2==1)
                    fout<<(i)<<" ";
            }
        fout<<endl;

    }
    fin.close();
    fout.close();
    return 0;
}
