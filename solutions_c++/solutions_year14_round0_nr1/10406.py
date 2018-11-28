#include<iostream>
using namespace std;
int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        int a1,a2;
        int ar1[5][5];
        int ar2[5][5];
        cin>>a1;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                cin>>ar1[i][j];
            }
        }
        cin>>a2;
        for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {
                cin>>ar2[i][j];
            }
        }
        int count=0;
        int pos;
         for(int i=1;i<=4;i++)
        {
            for(int j=1;j<=4;j++)
            {

                if(ar1[a1][i]==ar2[a2][j])
                {
                    count++;

                    pos=ar1[a1][i];
                }
            }
        }
        if(count==0)
        {
            cout<<"case #"<<t<<": "<<"Volunteer cheated!\n";
        }
       else if(count==1)
        {
            cout<<"case #"<<t<<": "<<pos<<"\n";
        }
        else
        {
            cout<<"case #"<<t<<": "<<"Bad magician!\n";
        }
    }
}
