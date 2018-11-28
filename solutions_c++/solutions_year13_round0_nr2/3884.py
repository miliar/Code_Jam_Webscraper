#include<fstream>
#include<iostream>
using namespace std;
int min1(int q,int w)
{
    if(q<w)
    return q;
    return w;
}
int main()
{
    int t,i,j,u,p,m,n,flag;
    int r[100],c[110],a[110][110];
    //scanf("%t");
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    fin>>t;
    for(u=1;u<=t;u++)
    {
        fin>>m>>n;
        for(i=1;i<=m;i++)
        {
            r[i]=0;
            for(j=1;j<=n;j++)
            {
                fin>>a[i][j];
                c[j]=0;
            }
        }
        for(i=1;i<=m;i++)
        {
            for(j=1;j<=n;j++)
            {
                if(a[i][j]>r[i])
                r[i]=a[i][j];
                if(a[i][j]>c[j])
                c[j]=a[i][j];
            }
        }
        flag=0;
        for(i=1;i<=m;i++)
        {
            for(j=1;j<=n;j++)
            {
                p=min1(r[i],c[j]);
                if(a[i][j]!=p)
                {
                    flag=1;
                    break;
                }
            }
        }
        if(flag==0)
        fout<<"Case #"<<u<<": YES\n";
        else
        fout<<"Case #"<<u<<": NO\n";
    }
}
