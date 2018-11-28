#include<iostream>
#include<cstring>
using namespace std;
void solve(int tc)
{
    int used[220];
    memset(used,0,sizeof(used));
    int ans;
    int grid[220][202];
    cin>>ans;
    for(int i=1;i<=4;i++)
    {
        for(int j=1;j<=4;j++)
        {
            cin>>grid[i][j];//cout<<grid[i][j]<<" ";
            if(i==ans)used[grid[i][j]]++;
        }//cout<<endl;
    }
    //for(int i=1;i<=4;i++)used[grid[ans][i]]++;
    cin>>ans;
    //cout<<endl;
    for(int i=1;i<=4;i++)
    {
        for(int j=1;j<=4;j++)
        {
            cin>>grid[i][j];//cout<<grid[i][j]<<" ";
            if(i==ans)used[grid[i][j]]++;
        }//cout<<endl;
    }
    //for(int i=1;i<=4;i++)used[grid[ans][i]]++;
    int o=-1;
    for(int i=1;i<=16;i++)
    {
        //cout<<used[i]<<" ";
        if(used[i]>=2)
        {
            if(o==-1)o=i;
            else {cout<<"Case #"<<tc<<": Bad magician!\n";return;}
        }
    }
    if(o==-1){cout<<"Case #"<<tc<<": Volunteer cheated!\n";return;}
    cout<<"Case #"<<tc<<": "<<o<<"\n";
}
int main()
{
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        solve(i);
    }
}
