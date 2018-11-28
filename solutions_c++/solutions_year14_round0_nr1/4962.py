#include<iostream>
using namespace std;
int main()
{
    int t,o;
    cin>>t;
    for(o=1;o<=t;o++)
    {
        int i,j,a,b,c[5][5],d[5][5];
        cin>>a;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            cin>>c[i][j];
        }
        cin>>b;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            cin>>d[i][j];
        }
        int count=0,flag=0;
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
            if(c[a][i]==d[b][j])
            {
                flag=c[a][i];
                count++;
                break;
            }
            }

        }
        if(count==0)
        {
            cout<<"Case #"<<o<<": Volunteer cheated!\n";

        }
        else if(count==1)
        {
            cout<<"Case #"<<o<<": "<<flag<<"\n";
        }
       else if(count>1)
        {
            cout<<"Case #"<<o<<": Bad magician!\n";
        }

            }
            return 0;
}
