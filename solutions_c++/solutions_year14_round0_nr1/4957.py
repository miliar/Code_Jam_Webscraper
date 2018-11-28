#include<iostream>
using namespace std;

int main()
{
    int t,k;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        int row1,row2,i,j,a[5][5],b[5][5];
        cin>>row1;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin>>a[i][j];
            }
        }
        cin>>row2;
         for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin>>b[i][j];
            }
        }
        int count=0,temp;
         for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(a[row1][i]==b[row2][j])
                {
                	count++;
                	temp=a[row1][i];
                }

            }

        }
        if(count==1)
         cout<<"Case #"<<k<<":"<<" "<<temp<<"\n";
       else if(count>1)
       cout<<"Case #"<<k<<":"<<" "<<"Bad magician!"<<"\n";
       else
       cout<<"Case #"<<k<<":"<<" "<<"Volunteer cheated!"<<"\n";
    }
    return 0;
}
