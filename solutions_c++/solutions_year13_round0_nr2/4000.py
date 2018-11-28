#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
     freopen("B-large.in","r", stdin);
     freopen("output.in","w", stdout);
    int t;
    cin>>t;
    int c=t;
    int a[100][100];
    while(t--)
    {
        int n,m;
        cin>>n>>m;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
            cin>>a[i][j];
        }
        int flag=1;
        for(int i=0;i<n;i++)
        {
            int max=a[i][0];
            for(int j=0;j<m;j++)
            {
                if(max<a[i][j])
                {
                    max=a[i][j];
                }
            }
            for(int j=0;j<m;j++)
            {
                if(a[i][j]<max)
                {
                    for(int k=0;k<n;k++)
                    {
                        if(a[k][j]>a[i][j])
                        {
                            flag=0;
                            break;
                        }
                    }
                }
                if(flag==0)
                {
                    break;
                }
            }
            if(flag==0)
                {
                    break;
                }
        }
     cout<<"Case #"<<c-t<<": ";
     if(flag)
     cout<<"YES"<<endl;
     else
     cout<<"NO"<<endl;
    }
}
