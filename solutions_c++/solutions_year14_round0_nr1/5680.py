#include<iostream>
using namespace std;
int main()
{
    int t,i,j,n,r1,r2,ct,x,value,temp[17];
    cin>>t;
    n=t;
    while(t--)
    {

        for(i=0;i<=16;i++){temp[i]=5;}
        cin>>r1;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>x;
                if(i==r1-1)
                {
                    temp[x]=3;
                }
            }
        }
        cin>>r2;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>x;
                if(i==r2-1)
                {
                    temp[x]-=1;
                }
            }
        }
        ct=0;
        for(i=1;i<=16;i++)
        {
            if(temp[i]==2){value=i;ct++;}
        }
        cout<<"Case #"<<n-t<<": ";
        if(ct==1){cout<<value<<endl;}
        else if(ct==0){cout<<"Volunteer cheated!"<<endl;}
        else cout<<"Bad magician!"<<endl;
    }
    return 0;
}
