#include<cstdio>
#include<iostream>

using namespace std;

int check(int a[][102],int i,int j, int n, int m)
{
    int l,x=0;
    for(l=0;l<n;l++)
    {
        if(a[l][j]>a[i][j])
        {
            x=1;
            break;
        }
    }
    if(x==1)
    {
        for(l=0;l<m;l++)
        {
            if(a[i][l]>a[i][j])
                return 1;
        }
    }
    return 0;
}
int main()
{
    freopen("B-large.txt","r",stdin);
    freopen("Q2out.txt","w",stdout);
    int test,t;
    cin>>test;
    for(t=1;t<=test;++t)
    {
        int n,m,i,j,a[102][102];
        bool flag=false;
        cin>>n>>m;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            cin>>a[i][j];
        }
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(check(a,i,j,n,m)==1)
                {
                    flag=true;
                    break;
                }
            }
            if(flag)
            break;
        }
        if(flag)
            cout<<"Case #"<<t<<": NO"<<endl;
        else
            cout<<"Case #"<<t<<": YES"<<endl;
    }
    return 0;
}
