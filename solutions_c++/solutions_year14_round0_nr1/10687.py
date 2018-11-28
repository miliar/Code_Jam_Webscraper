#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;

    for(int i=1;i<=n;i++)
    {
            int row1=0,row2=0,flag=0,chosen=0;
            cin>>row1;
            int a[4][4],b[4][4];
            for(int j=0;j<4;j++)
            {
                   for(int k=0;k<4;k++)
                   {
                           cin>>a[j][k];
                   }
            }
            cin>>row2;
            for(int j=0;j<4;j++)
            {
                   for(int k=0;k<4;k++)
                   {
                           cin>>b[j][k];
                   }
            }
            for(int j=0;j<4;j++)
            {
                    for(int k=0;k<4;k++)
                    {
                            if( a[row1-1][j]==b[row2-1][k] )
                            {
                                flag++;
                                chosen=a[row1-1][j];
                            }
                    }

            }
            if(flag==0)
            cout<<"Case #"<<i<<": Volunteer cheated!";
            else if(flag==1)
            cout<<"Case #"<<i<<": "<<chosen;
            else if(flag>1)
            cout<<"Case #"<<i<<": Bad magician!";
            if(i<100)
                cout<<endl;
    }

}
