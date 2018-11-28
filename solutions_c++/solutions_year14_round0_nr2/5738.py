#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int tst;
    cin>>tst;
    double c[tst+1],f[tst+1],x[tst+1],nf;
    double cs[tst+1][2001];
    for(int i=1;i<=tst;i++)
    {
        for(int j=1;j<=2000;j++)
        {
            cs[i][j]=0;
        }
    }
    for(int i=1;i<=tst;i++)
    {
        cin>>c[i];
        cin>>f[i];
        cin>>x[i];
    }
    for(int i=1;i<=tst;i++)
    {
        for(int j=1;j<=2000;j++)
        {
            nf=2;
            if(j==1)
            {
                cs[i][j]=x[i]/2;
            }
            else if(j>1)
            {
                for(int k=1;k<=j;k++)
                {
                    if(k<j)
                    {
                        cs[i][j]=cs[i][j]+(c[i]/nf);
                        nf=nf+f[i];
                    }
                    else if(k==j)
                    {
                        cs[i][j]=cs[i][j]+(x[i]/nf);
                    }
                }
                if(cs[i][j]>=cs[i][j-1])
                {
                    cout<<"Case "<<"#"<<i<<": ";
                    cout<<fixed<<setprecision(7)<<cs[i][j-1];
                    //cout.precision(7)<<cs[i][j-1];
                    cout<<endl;
                    break;
                }
            }


        }
    }
    return 0;
}

