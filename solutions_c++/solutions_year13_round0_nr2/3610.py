#include <fstream>
using namespace std;

ifstream f("input.in");
ofstream g("output.out");

int b[101];

int main()
{
    short i,j,i1,i2,m,n,t,t1,e,min,a[100][100];
    f>>t;
    t1=t;
    while(t>0)
    {
        f>>n>>m;
        e=1;
        min=101;
        for(i=0;i<n;++i)
        {
            for(j=0;j<m;++j)
            {
                f>>a[i][j];
                if(a[i][j]<min) min=a[i][j];
                b[a[i][j]]=1;
            }
        }
        for(i2=min;i2<=100&&e;i2++)
        {
            if(b[i2]) min=i2;
            {
                for(i=0;i<n&&e;++i)
                {
                    for(j=0;j<m&&e;++j)
                    {
                        if(a[i][j]==min)
                        {
                            for(i1=0;i1<n&&e;++i1)
                            {
                                if(a[i1][j]>min) e=0;
                            }
                            if(e) for(i1=0;i1<n;++i1) a[i1][j]=0;
                            if(!e)
                            {
                                e=1;
                                for(i1=0;i1<m&&e;++i1)
                                {
                                    if(a[i][i1]>min) e=0;
                                }
                                if(e) for(i1=0;i1<m;++i1) a[i][i1]=0;
                            }
                        }
                    }
                }
            }
        }
        for(i=1;i<=100;++i) b[i]=0;
        --t;
        g<<"Case #"<<t1-t<<": ";
        if(e) g<<"YES"<<'\n';
        else g<<"NO"<<'\n';
    }
    f.close();
    g.close();
    return 0;
}
