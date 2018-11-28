#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    int first[4][4],second[4][4],i,j,c,uno,duo,count,prev,test_case;
    cin>>test_case;
    for(c=0;c<test_case;c++)
    {
        count = 0;
        cin>>uno;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                cin>>first[i][j];
        }
        cin>>duo;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
                cin>>second[i][j];
        }
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(!(first[uno-1][i]-second[duo-1][j]))
                {
                    count++;
                    prev=first[uno-1][i];
                }
            }
        }
        if(count==0)
            cout<<"Case #"<<(c+1)<<": Volunteer cheated!\n";
        else if(count==1)
            cout<<"Case #"<<(c+1)<<": "<<prev<<"\n";
        else
            cout<<"Case #"<<(c+1)<<": Bad magician!\n";
    }
    return 0;

}
