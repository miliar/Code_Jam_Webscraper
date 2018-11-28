#include <iostream>

using namespace std;

int main()
{
    int T,i,j,y,k,ans=0,B1[4][4],B2[4][4],a1,a2,row[4];
    bool bb=true;
    cin>>T;
    for(i=1;i<=T;i++)
    {
        ans=0;
        cin>>a1;
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                cin>>B1[j][k];
            }
        }
        cin>>a2;
        for(j=0;j<4;j++)
        {
            for(k=0;k<4;k++)
            {
                cin>>B2[j][k];
            }
        }
        for(j=0;j<4;j++)
        {
           for(k=0;k<4;k++)
           {
                if(B1[a1-1][k]==B2[a2-1][j])
                {
                    ans++;
                    y=B1[a1-1][k];
                }
           }
        }
        if(ans==1)
        {
            cout<<"Case #"<<i<<": "<<y<<endl;
        }
        else if(ans==0)
        {
            cout<<"Case #"<<i<<": "<<"Volunteer cheated!\n";
        }
        else
        {
            cout<<"Case #"<<i<<": "<<"Bad magician!\n";
        }
    }
    return 0;
}
