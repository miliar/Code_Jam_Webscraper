#include<stdio.h>
#include<iostream>

using namespace std;
int main()
{
    int t,i,j,k,n,m,l,r;
    int a[4][4],b[4][4];
    cin>>t;
    for(r=1;r<=t;r++)
    {
        cin>>n;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>a[i][j];
        cin>>m;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>b[i][j];
                k=0;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                if(a[n-1][i] == b[m-1][j])
                    {
                        k++;
                        l=a[n-1][i];
                    }
        if(k>1)
            cout<<"Case #"<<r<<": Bad magician!"<<endl;
        else if(k==0)
            cout<<"Case #"<<r<<": Volunteer cheated!"<<endl;
        else
            cout<<"Case #"<<r<<": "<<l<<endl;
    }
    return 0;
}
