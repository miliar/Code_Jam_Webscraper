#include<strings.h>
#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    int ts,z=1;
    ifstream cinner("B-large.in",ios::in);
    cinner>>ts;
    cout<<ts;
    ofstream coutter("out3.txt",ios::out);
    for(; z<=ts; z++)
    {
        int m,n,h[101][101],maxr[101],maxc[101],i,j,flag=0;
        cinner>>m>>n;
        for(i=1; i<=m; i++)
        {
            maxr[i]=0;
            for(j=1; j<=n; j++)
            {
                cinner>>h[i][j];
                //cout<<h[i][j]<<' ';
                if(flag)continue;
                if(i==1)
                {
                    maxc[j]=0;
                }
                if(maxr[i]<h[i][j])
                {
                    maxr[i]=h[i][j];
                }
                if(maxc[j]<h[i][j])
                {
                    maxc[j]=h[i][j];
                }
                if((h[i][j]<maxr[i])&&(h[i][j]<maxc[j]))
                {
                    coutter<<"Case #"<<z<<": NO\n";
                    ++flag;
                }
            }
            //cout<<endl;
        }
        if(flag==0)
            for(j=1; j<=n; j++)
            {
                for(i=1; i<=m; i++)
                {
                    if(h[i][j]<maxr[i]&&h[i][j]<maxc[j])
                    {

                        coutter<<"Case #"<<z<<": NO\n";
                        flag++;
                        i=m;
                        j=n;
                    }
                }
            }
        if(flag==0)
            coutter<<"Case #"<<z<<": YES\n";
    }
    return 0;
}
