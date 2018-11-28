#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    int i,j,t,p,n,m,k,an;
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    fin>>t;
    for(p=1;p<=t;p++)
    {
        fin>>n>>m;
        int a[n][m];
        for(i=0;i<n;i++)
        for(j=0;j<m;j++)
        fin>>a[i][j];

        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                an=0;
                for(k=0;k<m;k++)
                if(a[i][k]>a[i][j])
                break;
                if(k==m)
                {an=1; continue;}

                for(k=0;k<n;k++)
                if(a[k][j]>a[i][j])
                break;
                if(k==n)
                {an=1; continue;}

                if(an==0)
                break;
            }
            if(an==0)
            break;
        }
        if(an==1)
         fout<<"Case #"<<p<<": YES\n";
         else
          fout<<"Case #"<<p<<": NO\n";
    }
    return 0;
}
