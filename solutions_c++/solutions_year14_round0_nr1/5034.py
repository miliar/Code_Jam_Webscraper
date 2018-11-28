#include<iostream>

using namespace std;

int main()
{
    int t,x,y,co,no,i,j,k;
    int n[4][4];
    cin>>t;
    for(k=1;k<=t;k++)
    {
        co=0;
        int c[17]={0};
        cin>>x;
        x--;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>n[i][j];
                if(i==x)
                {
                    c[n[i][j]]++;
                }
            }
        }

        cin>>y;
        y--;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>n[i][j];
                if(i==y)
                {
                    c[n[i][j]]++;
                    if(c[n[i][j]]==2)
                        {co++;
                        no=n[i][j];}
                }
            }
        }

        if(co==1)
        {
            cout<<"Case #"<<k<<": "<<no<<endl;
        }
        else if(co==0)
        {
            cout<<"Case #"<<k<<": Volunteer cheated!\n";
        }
        else
        {
            cout<<"Case #"<<k<<": Bad magician!\n";
        }
    }
    return 0;
}
