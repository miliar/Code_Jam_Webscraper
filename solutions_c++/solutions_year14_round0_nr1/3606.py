/*
Mid_Night
C++
*/
#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
#include<vector>
#include<math.h>
#include<stack>
#define f0(i,n) for(int i=0;i<=n;i++)
#define fn(i,n) for(int i=n;i>0;i--)
#define f1(i,a,n) for(int i=a;i<=n;i++)
#define f2(i,a,n) for(int i=a;i>=n;i--)

using namespace std;

int main()
{
    ofstream fout ("frac1.out");
    ifstream fin ("frac1.in");
    int t,T,n,n1,i,j,k,a[4][4],b[4][4],c;
    fin>>T;
    for(t=1;t<=T;t++)
    {
        c=0;
        fin>>n;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                fin>>a[i][j];
            }
        }
        fin>>n1;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                fin>>b[i][j];
            }
        }
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a[n-1][i]==b[n1-1][j])
                {
                    c++;
                    k=a[n-1][i];
                }
            }
        }
        if(c>1)
        {
            fout<<"Case #"<<t<<": "<<"Bad magician!\n";
        }
        else if(c==0)
        {
            fout<<"Case #"<<t<<": "<<"Volunteer cheated!\n";
        }
        else
        {
            fout<<"Case #"<<t<<": "<<k<<endl;
        }
    }
    return 0;
}
