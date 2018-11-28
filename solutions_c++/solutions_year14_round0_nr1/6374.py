#include<iostream>
#include<stdio.h>
using namespace std;

main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A-small.out","w+",stdout);

    int i,j,n,k,p,w,m,t,a[5][5],b[5][5];
    cin>>n;
    for(j=0; j<n; j++)
    {
        cin>>k;
        for(i=0; i<4; i++)
        {
            for(p=0; p<4; p++)
            {
                cin>>a[i][p];
            }
        }
        cin>>m;
        for(i=0; i<4; i++)
        {
            for(p=0; p<4; p++)
            {
                cin>>b[i][p];
            }
        }
        t=0;
        w=0;
        k=k-1;
        m=m-1;
        for(i=0; i<4; i++)
        {
            for(p=0; p<4; p++)
            {
                if((t==0)&&(a[k][i]==b[m][p])){t=a[k][i]; continue;}
                if((t>0)&&(a[k][i]==b[m][p]))w=1;
            }
        }
        if(t==0)cout<<"Case #"<<j+1<<": "<<"Volunteer cheated!"<<endl;
        if((w==1)&&(t>0))cout<<"Case #"<<j+1<<": "<<"Bad magician!"<<endl;
        if((w==0)&&(t>0))cout<<"Case #"<<j+1<<": "<<t<<endl;
    }
   // system("pause");
}
