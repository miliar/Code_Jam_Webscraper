#include<iostream>
using namespace std;
int t,r;
int a[8][8],m[32];
void scan()
{
    int i,j;
    cin>>r;
    for(i=1;i<=4;i++)
    for(j=1;j<=4;j++)
    cin>>a[i][j];
}
void solve(int x)
{
    int i,j,l=0,p=4;
    scan();
    for(i=1;i<=4;i++)
    {m[i]=a[r][i];}
    
    scan();
    for(i=1;i<=4;i++)
    {
        for(j=1;j<=4;j++)
        {
            if(m[i]==a[r][j]){l=1;break;}
        }
        if(l==0){m[i]=0;p--;}
        l=0;
    }
    cout<<"Case #";
    cout<<x<<": ";
    if(p==1)
    {
        for(i=1;i<=4;i++)if(m[i]!=0)cout<<m[i]<<"\n";
    }
    if(p>1)cout<<"Bad magician!\n";
    if(p==0)cout<<"Volunteer cheated!\n";
}
int main()
{
    cin>>t;
    int i;
    for(i=1;i<=t;i++)solve(i);
    return 0;
}