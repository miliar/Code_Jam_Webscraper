#include<iostream>
#include<cstdio>
using namespace std;
int n,m,te,t[111][111],out,g;
int main()
{
    ios_base::sync_with_stdio(0);
    cin>>te;
    for(int i=1;i<=te;i++)
    {
            cin>>n>>m;
            for(int j=1;j<=n;j++)
            {
                    for(int k=1;k<=m;k++)
                    cin>>t[j][k];
                    }
            out=0;
            for(int j=1;j<=n;j++)
            {
                    for(int k=1;k<=m;k++)
                    {
                            g=0;
                            for(int v=1;v<=n;v++)
                            if(t[v][k]>t[j][k])
                            {
                                 g++;
                                 break;
                            }
                            for(int v=1;v<=m;v++)
                            if(t[j][v]>t[j][k])
                            {
                                 g++;
                                 break;
                            }
                            if(g==2)
                            {
                                    out=1;
                                    break;
                            }
                    }
                    if(out==1)
                    break;
            }
            cout<<"Case #"<<i<<": ";
            if(out==1)
            cout<<"NO"<<endl;
            else
            cout<<"YES"<<endl;
    }
    cin.ignore(2);
    return 0;
}
