#include<bits/stdc++.h>
using namespace std;
int main()
{
freopen ("input.txt", "r", stdin);
freopen ("output.txt", "w", stdout);
int ans1,ans2,t,temp,i,j,k;
cin>>t;
for(j=1;j<=t;j++)
{
    int arr[17]={0};
    cin>>ans1;
    for(k=0;k<4;k++)
    {
    for(i=0;i<4;i++)
    {
        cin>>temp;
        if(k+1==ans1)
            arr[temp]++;
    }
    }
    cin>>ans2;
    for(k=0;k<4;k++)
    {
    for(i=0;i<4;i++)
    {
        cin>>temp;
        if(k+1==ans2)
            arr[temp]++;
    }
    }
    int c2=0,ans;
    for(i=1;i<=16;i++)
    {
        if(arr[i]==2)
            {c2++;ans=i;}
    }
    if(c2==0)
        cout<<"Case #"<<j<<": Volunteer cheated!"<<endl;
    else if(c2==1)
        cout<<"Case #"<<j<<": "<<ans<<endl;
    else
        cout<<"Case #"<<j<<": Bad magician!"<<endl;
}
}
