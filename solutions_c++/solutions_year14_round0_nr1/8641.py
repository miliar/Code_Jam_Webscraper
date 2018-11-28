#include<iostream>
using namespace std;

int main()
{
    int i,j,c,t,temp,ctr,ra,rb,a[4][4],b[4][4];
    cin>>t;
    for(c=1; c<=t; c++)
    {
        ctr=0;
        cin>>ra;
        for(i=0; i<4; i++)
        {
            for(j=0;j<4; j++)
            {
                cin>>a[i][j];
            }
        }

        cin>>rb;
        for(i=0; i<4; i++)
        {
            for(j=0;j<4; j++)
            {
                cin>>b[i][j];
            }
        }

        for(i=0; i<4; i++)
        {
            for(j=0;j<4; j++)
            {
                if(a[ra-1][i]==b[rb-1][j])
                {
                    temp = a[ra-1][i];
                    ctr++;
                }
            }
        }

        if(ctr==1)
        {
            cout<<"Case #"<<c<<": "<<temp<<endl;
        }
        else if(ctr==0)
        {
            cout<<"Case #"<<c<<": "<<"Volunteer cheated!"<<endl;
        }
        else
        {
            cout<<"Case #"<<c<<": "<<"Bad magician!"<<endl;
        }

    }
    return 0;
}
