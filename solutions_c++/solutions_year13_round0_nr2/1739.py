#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<queue>
#include<stack>
#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
const int M=100;
int main()
{
    int t;
    int a[M][M];
    bool v[M][M];
    bool num[M];
//    freopen("B-large.in","r",stdin);
//    freopen("B-large.txt","w",stdout);

    while(cin>>t)
    {
        int n,m;
        for(int i=1;i<=t;i++)
        {
            cin>>n>>m;
            bool flag=true;
            memset(v,false,sizeof(v));
            memset(num,false,sizeof(num));
            for(int j=0;j<n;j++)
            {
                for(int k=0;k<m;k++)
                {
                    int temp;
                    cin>>temp;
                    a[j][k]=temp;
                    num[temp]=true;
                }
            }
            for(int x=1;x<=100;x++)
            {
                if(num[x])
                {
                    memset(v,false,sizeof(v));
                    for(int j=0;j<n;j++)
                    {
                        for(int k=0;k<m;k++)
                        {
                            if(a[j][k]==x&&!v[j][k])
                            {
                                bool flagj=true;
                                bool flagk=true;
                                for(int z=0;z<n;z++)
                                {
                                    if(a[z][k]>x)
                                    {
                                        flagj=false;
                                        break;
                                    }
                                }
                                if(flagj)
                                {
                                    for(int z=0;z<n;z++)
                                    {
                                        v[z][k]=true;
                                    }
                                }
                                for(int z=0;z<m;z++)
                                {
                                    if(a[j][z]>x)
                                    {
                                        flagk=false;
                                        break;
                                    }
                                }
                                if(flagk)
                                {
                                    for(int z=0;z<m;z++)
                                    {
                                        v[j][z]=true;
                                    }
                                }
                                if(!flagj&&!flagk)
                                {
                                    flag=false;
                                    break;
                                }
                            }
                        }
                        if(!flag)
                        {
                            break;
                        }
                    }
                    if(!flag)
                    {
                        break;
                    }
                }
            }
            if(flag)
            {
                cout<<"Case #"<<i<<": "<<"YES"<<endl;
            }
            else
            {
                cout<<"Case #"<<i<<": "<<"NO"<<endl;
            }
        }
    }
    return 0;
}
