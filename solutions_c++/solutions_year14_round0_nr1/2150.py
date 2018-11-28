#include<stdio.h>
#include<algorithm>
#include<iostream>
using namespace std;
int a[5][5];
int b[5][5];
int main()
{
    int i,j,t,n,m,N,s,k;
    
    freopen("A-small-attempt2.in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin>>t;
    N=t;
    while(t--)
    {
        cin>>n;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
                cin>>a[i][j];
        }
        cin>>m;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin>>b[i][j];
            }
        }
        s=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(a[n][i]==b[m][j])
                {
                    k=a[n][i];
                    s++;
                    break;
                }
            }
        }
        if(s==0)
            cout<<"Case #"<<N-t<<": Volunteer cheated!\n";
        else if(s==1)
            cout<<"Case #"<<N-t<<": "<<k<<endl;
        else
        {
            cout<<"Case #"<<N-t<<": Bad magician!\n";
        }
    }
    return 0;
}