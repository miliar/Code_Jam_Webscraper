#include<iostream>
#include<stdio.h>

using namespace std;
int main()
{
    int t;
    int k=1;
    cin>>t;
    int a[16],b[16];
    for(k=1;k<=t;k++){
    int vis[17]={0};
    int x,y;
    cin>>x;
    int i,j;
    for(i=0;i<16;i++)scanf("%d",&a[i]);
    cin>>y;
    for(i=0;i<16;i++)scanf("%d",&b[i]);
    for(i=4*(x-1),j=0;j<4;i++,j++)vis[a[i]]++;
    for(i=4*(y-1),j=0;j<4;i++,j++)vis[b[i]]++;
    int count=0,ans;
    for(i=1;i<17;i++)if(vis[i]==2){ans=i;count++;}
    if(count==1)cout<<"Case #"<<k<<": "<<ans<<'\n';
    else if(count==0)cout<<"Case #"<<k<<": Volunteer cheated!\n";
    else cout<<"Case #"<<k<<": Bad magician!\n";
    }
}
