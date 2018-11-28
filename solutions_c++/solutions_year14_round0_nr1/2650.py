#include <iostream>

using namespace std;

int main()
{
    int store[5][5],data1=0,data2=0,store2[5][5],compA[5],compB[5],total=0,ans=0;
    int test;
    cin>>test;

for(int run=1;run<=test;run++)
{
    ans=0;
    total=0;
    cin>>data1;
    for(int i=1;i<=4;i++)
    {
        for (int j=1;j<=4;j++)
        {
            cin>>store[i][j];
        }
    }
    for(int i=1;i<=4;i++)
    {
        compA[i]=store[data1][i];
    //    cout<<compA[i]<<endl;
    }

    cin>>data2;
    for(int i=1;i<=4;i++)
    {
        for (int j=1;j<=4;j++)
        {
            cin>>store2[i][j];
        }
    }
    for(int i=1;i<=4;i++)
    {
        compB[i]=store2[data2][i];
    // cout<<compB[i]<<endl;
    }
    for(int i=1;i<=4;i++)
    {
        for(int j=1;j<=4;j++)
        {
            if(compA[j]==compB[i])
            {
                total++;
                ans=compA[j];
            }
        }
    }
    //cout<<"Total = "<<total;
    if(total==1)
    {
     cout<<"Case #"<<run<<": "<<ans<<endl;
    }
    else if(total>1)
    {
     cout<<"Case #"<<run<<": Bad magician!"<<endl;
    }
    else if(total==0)
    {
     cout<<"Case #"<<run<<": Volunteer cheated!"<<endl;
    }
}

    return 0;
}
