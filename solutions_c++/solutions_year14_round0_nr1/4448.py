#include<iostream>
using namespace std;
int main()
{
        int tc;
        cin>>tc;
        int s=5;    //size
        int i,j,k,grid[5][5]={{0,},};
        int first,second;
        for(i=0;i<tc;i++)
        {
                cin>>first;
                for(j=1;j<s;j++)
                    for(k=1;k<s;k++)
                        cin>>grid[j][k];

                int row[5]={0,};
                for(j=1;j<s;j++)
                    row[j]=grid[first][j];
                cin>>second;
                 for(j=1;j<s;j++)
                    for(k=1;k<s;k++)
                        cin>>grid[j][k];
                int ct=0,number;
                for(j=1;j<s;j++)
                {
                    for(k=1;k<s;k++)
                    {
                            if(row[j]==grid[second][k])
                            {
                                number=row[j];
                                ct++;
                            }
                    }
                }
                if(ct==0)
                    cout<<"Case #"<<i+1<<": Volunteer cheated!\n";
                else if(ct==1)
                    cout<<"Case #"<<i+1<<": "<<number<<"\n";
                else if(ct>1)
                    cout<<"Case #"<<i+1<<": Bad magician!\n";
        }
        return 0;
}
