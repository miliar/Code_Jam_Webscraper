#include <iostream>
using namespace std;
int main()
{
    int n1,n2,i,j,t,co=0,c1=0,temp;
    int a[4][4],b[4][4],c[4],d[4];
    cin>>t;
    while(t--)
    {
        co++;
        c1=0;
        cin>>n1;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin>>a[i-1][j-1];
            }
        }
        cin>>n2;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                cin>>b[i-1][j-1];
            }
        }
        for(i=1;i<=4;i++)
        {
            c[i-1]=a[n1-1][i-1];
        }

        for(i=1;i<=4;i++)
        {
            d[i-1]=b[n2-1][i-1];
        }

        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                if(c[i-1]==d[j-1])
                {
                    c1++;
                    temp=c[i-1];
                    break;
                }
            }
        }
        if(c1==0)
            cout<<"Case #"<<co<<": Volunteer cheated!"<<endl;
        else if(c1==1)
            cout<<"Case #"<<co<<": "<<temp<<endl;
        else
            cout<<"Case #"<<co<<": Bad magician!"<<endl;
    }
    return 0;
}
