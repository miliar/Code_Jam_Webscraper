#include<iostream>

using namespace std;

int tstcss,nt;
int n,m,i,j,k,a[200][200];
bool t1,t2,bl;

int main()
{
    cin>>tstcss;
    nt=0;
    while (tstcss--)
    {
        nt++;
        cin>>n>>m;
        for (i=0;i<n;i++)
        {
            for (j=0;j<m;j++)
            {
                cin>>a[i][j];
            }
        }
        bl=true;
        for (i=0;i<n;i++)
        {
            for (j=0;j<m;j++)
            {
                t1=false;t2=false;
                for (k=0;k<m;k++)
                {
                    if (a[i][k]>a[i][j])
                    {
                        t1=true;
                        break;
                    }
                }
                for (k=0;k<n;k++)
                {
                    if (a[k][j]>a[i][j])
                    {
                        t2=true;
                        break;
                    }
                }
                if (t1&&t2) {bl=false;break;}
            }
            if (!bl) break;
        }
        cout<<"Case #"<<nt<<": ";
        if (bl) cout<<"YES"<<endl; else cout<<"NO"<<endl;
    }
    return 0;
}
                
