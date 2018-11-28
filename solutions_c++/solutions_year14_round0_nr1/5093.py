#include<iostream>
using namespace std;

int main()
{
 int t,a1,a2,b1[4][4],b2[4][4],a,i,j,k,l;
    cin>>t;
    l=t;
    while(t--)
    {
        a=0;
    cin>>a1;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
          cin>>b1[i][j];
    cin>>a2;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
          cin>>b2[i][j];

for(i=0;i<4;i++)
{
    for(j=0;j<4;j++)
        if(b1[a1-1][i]==b2[a2-1][j]){a++;k=b1[a1-1][i];}
}
    cout<<"Case #"<<l-t<<": ";
    if(a==0)cout<<"Volunteer cheated!\n";
    else if(a==1)cout<<k<<"\n";
    else cout<<"Bad magician!\n";
    }
    return 0;
}
