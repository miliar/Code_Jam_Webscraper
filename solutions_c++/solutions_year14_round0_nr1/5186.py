#include<iostream>
using namespace std;

int main()
{
    int t,l=0;
    cin>>t;
    while(t--)
    {
        l++;
        int a,b;
        bool c[16]={0};
        int ar[4][4];
        int ans,i,j,count=0;
        cin>>a;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            {
               cin>>ar[i][j];
               if(i==(a-1))
                    c[ar[i][j]-1]=1;
            }
        cin>>b;
        for(i=0;i<4;i++)
            for(j=0;j<4;j++)
            {
               cin>>ar[i][j];
               if(i==(b-1))
                {
                        if(c[ar[i][j]-1]==1)
                        {
                            count++;
                            ans=ar[i][j];
                        }
                }
            }
        if(count==1)
            cout<<"Case #"<<l<<": "<<ans<<endl;
        else if(count>1)
            cout<<"Case #"<<l<<": Bad magician!\n";
        else
            cout<<"Case #"<<l<<": Volunteer cheated!\n";
    }
    return 0;
}
