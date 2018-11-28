#include <iostream>
#include <string>

using namespace std;

int main()
{
    int t,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        int ans=0,x,y,num=0;
        int a[4][4],b[4][4];
        cin>>x;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                cin>>a[j][k];
            }
        }
        cin>>y;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                cin>>b[j][k];
            }
        }
        x--;
        y--;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                if(a[x][j]==b[y][k])
                {
                    num++;
                    ans=a[x][j];
                }
            }
        }

        if(num==0)
             cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
        else if(num==1)
             cout<<"Case #"<<i<<": "<<ans<<endl;
        else
             cout<<"Case #"<<i<<": Bad magician!"<<endl;
    }
    return 0;

}
