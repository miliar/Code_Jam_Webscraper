#include <iostream>
using namespace std;

int main()
{

    int n,m1,m2,i,j,k,a[4][4],b[4][4],p,t;

    cin>>n;

    for(i=0;i<n;i++)
    {

        cin>>m1;
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)   cin>>a[j][k];
        }

        cin>>m2;
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)   cin>>b[j][k];
        }

        p=0;

        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                if(a[m1-1][j]==b[m2-1][k])
                {
                    t=a[m1-1][j];
                    p++;
                }
            }
        }

        switch(p)
        {
        case 0:cout<<"Case #"<<i+1<<": Volunteer cheated!";break;
        case 1:cout<<"Case #"<<i+1<<": "<<t;break;
        default:cout<<"Case #"<<i+1<<": Bad magician!";break;
        }

        if(i<n-1) cout<<endl;

    }

    return 0;
}
