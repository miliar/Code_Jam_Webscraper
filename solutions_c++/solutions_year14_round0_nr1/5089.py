#include<iostream>
using namespace std;
int main()
{
    int T,r1,r2,a1[4][4],a2[4][4],count;
    cin>>T;
    for(int m=1;m<=T;m++)
    {
        cin>>r1;
        r1=r1-1;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            cin>>a1[i][j];
        }
        //for(int i=0;i<4;i++)
        //cout<<a1[r1][i]<<" ";
        cin>>r2;
        r2=r2-1;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            cin>>a2[i][j];
        }
        //for(int i=0;i<4;i++)
        //cout<<a2[r2][i]<<" ";
        count=0;
        int element;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(a1[r1][i]==a2[r2][j])
                {
                    count++;
                    element=a2[r2][j];
                 //   cout<<element<<" ";
                }
            }
        }
        if(count==1)
        cout<<"Case #"<<m<<": "<<element<<endl;
        else if(count>1)
        cout<<"Case #"<<m<<": Bad magician!"<<endl;
        else if(count==0)
        cout<<"Case #"<<m<<": Volunteer cheated!"<<endl;
    }
return 0;
}
