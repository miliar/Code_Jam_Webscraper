#include<iostream>
using namespace std;

int main()
{
    int t,count,answr,i,j,cs=0;
    int row1,row2,grid1[4][4],grid2[4][4];
    cin>>t;
    while(t)
    {
        cs++;
        count=0;
        cin>>row1;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>grid1[i][j];
            }
        }
        cin>>row2;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>grid2[i][j];
            }
        }
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(grid1[row1-1][i]==grid2[row2-1][j])
                {
                    count++;
                    answr=grid1[row1-1][i];
                }
            }
        }
        if(count==1)
        {
            cout<<"Case #"<<cs<<": "<<answr<<endl;
        }
        else if(count==0)
        {
            cout<<"Case #"<<cs<<": "<<"Volunteer cheated!"<<endl;
        }
        else
        {
            cout<<"Case #"<<cs<<": "<<"Bad magician!"<<endl;
        }
        t--;
    }
    return 0;

}
