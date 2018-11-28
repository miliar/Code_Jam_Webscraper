#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;
main()
{
    int a[4][4],b[4][4],i,j,r1,r2,t,k=0,cnt=0,val;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    while(k<t)
    {
        cnt=0;
        cin>>r1;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>a[i][j];
        cin>>r2;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
                cin>>b[i][j];
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a[r1-1][i]==b[r2-1][j])
                {   cnt++;
                    val=a[r1-1][i];
                }
            }
        }
        cout<<"Case #"<<k+1<<": ";
        if(cnt==0)
            cout<<"Volunteer cheated!\n";
        else if(cnt==1)
            cout<<val<<"\n";
        else
            cout<<"Bad magician!\n";
        k++;
    }
}