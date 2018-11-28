#include<cstdio>
#include<cstdlib>
#include<iostream>
using namespace std;
int main()
{
    long int A[120][120],B[120][120];
    long int i,j,k,t,T,n,m,count,max,x;
    cin>>t;
    T=t;
    while(t--)
    {
        cin>>n>>m;
        count=m*n;

        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                cin>>A[i][j];
                B[i][j]=0;
            }
        }

        for(i=1;i<=n;i++)
        {
            max=0;
            for(j=1;j<=m;j++)
            {
                if(A[i][j]>max)
                max=A[i][j];
            }
            A[i][0]=max;
        }
        for(i=1;i<=m;i++)
        {
            max=0;
            for(j=1;j<=n;j++)
            {
                if(A[j][i]>max)
                max=A[j][i];
            }
            A[0][i]=max;
        }

        //
        for(i=1;i<=n;i++)
        {
            max=A[i][0];
            for(j=1;j<=m;j++)
            {
                if(A[i][j]==max && B[i][j]==0)
                {
                    B[i][j]=1;
                    count--;
                }
            }
        }
        for(i=1;i<=m;i++)
        {
            max=A[0][i];
            for(j=1;j<=n;j++)
            {
                if(A[j][i]==max && B[j][i]==0)
                {
                    B[j][i]=1;
                    count--;
                }
            }
        }
/*
        for(i=1;i<=n;i++)
        {
            for(j=1;j<=m;j++)
            {
                cout<<B[i][j]<<" ";
            }
            cout<<"\n";
        }
*/
        if(count==0)
        cout<<"Case #"<<T-t<<": YES\n";
        else
        cout<<"Case #"<<T-t<<": NO\n";
    }
    return 0;
}
