#include<iostream>
using namespace std;
int t,n,m,a[8][8],b[8][8];

void read()
{
    int i,j;
    cin>>n;
    for (i=0;i<4;i++)
        for (j=0;j<4;j++) cin>>a[i][j];
    cin>>m;
    for (i=0;i<4;i++)
        for (j=0;j<4;j++) cin>>b[i][j];
    
}

void solve (int s)
{
    int i,j,br=0,ans;
    for (i=0;i<4;i++)
        for (j=0;j<4;j++)
            if (a[n-1][i]==b[m-1][j]) {br++;ans=a[n-1][i];}
    if (br==1) cout<<"Case #"<<s<<": "<<ans<<endl;
    if (br==0) cout<<"Case #"<<s<<": Volunteer cheated!"<<endl;
    if (br>1) cout<<"Case #"<<s<<": Bad magician!"<<endl;
}

int main()
{
    int i;
    cin>>t;
    for (i=1;i<=t;i++)
    {
        read();
        solve (i);
    }
    return 0;
}