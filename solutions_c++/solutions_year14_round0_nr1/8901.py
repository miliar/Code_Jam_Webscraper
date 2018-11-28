#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    freopen("example1.txt","r",stdin);
    freopen("output1.txt","w",stdout);
    int t;
    cin>>t;
    for(int k=1;k<=t;k++)
    {
        int a[4][4],b[4][4],x,y,z,count=0;
        cin>>x;
        for(int i =0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>a[i][j];
            }
        }
        cin>>y;
        for(int i =0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>b[i][j];
            }
        }
        for (int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {


            if(a[x-1][i]==b[y-1][j])
               {
                   z=a[x-1][i];
                count++;
               }
        }

    }
    if(count==0)
            cout<<"Case #"<<k<<": Volunteer cheated!\n";
       else if(count==1)
        cout<<"Case #"<<k<<": "<<z<<"\n";
        else cout<<"Case #"<<k<<": Bad magician!\n";
}
}
