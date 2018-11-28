#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("Output1.txt","w",stdout);
    int t,arr[20]={0},flag,ans,test=0,x;
    cin>>t;
    while(t--)
    {
        test++;
        memset(arr,0,sizeof(arr));
        cin>>ans;
        for(int i=1;i<=4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>x;
                if(i==ans)
                    arr[x]++;
            }
        }
        cin>>ans;
        for(int i=1;i<=4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>x;
                if(i==ans)
                    arr[x]++;
            }
        }
        flag=0;
        for(int i=1;i<=16;i++)
        {
            if(arr[i]==2)
            {
                flag++;
                ans=i;
            }
        }
        if(flag==1)cout<<"Case #"<<test<<": "<<ans<<endl;
        else if(flag==0)cout<<"Case #"<<test<<": "<<"Volunteer cheated!\n";
        else cout<<"Case #"<<test<<": "<<"Bad magician!\n";
    }
    return 0;
}
