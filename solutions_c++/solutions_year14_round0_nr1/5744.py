#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("output.out","w",stdout);
   int n,nz=1;
   cin>>n;
int ft,far[10][10],fj=0,fjs[10];
int st,sar[10][10],sj=0,sjs[10];
int cnt=0,com[4];
   while(n--)
{
    cin>>ft;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            cin>>far[i][j];
cin>>st;
for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            cin>>sar[i][j];
     //cout<<"****"<<ft<<"  "<<far[ft][0]<<"\n";
     for(int k=0;k<4;k++)
        for(int y=0;y<4;y++)
        if(far[ft-1][k]==sar[st-1][y]) com[cnt++]=far[ft-1][k];
cout<<"Case #"<<nz++<<": ";
if(cnt==0) cout<<"Volunteer cheated!\n";
else if(cnt>1) cout<<"Bad magician!\n";
else cout<<com[0]<<"\n";
cnt=0;
}
    return 0;
}
