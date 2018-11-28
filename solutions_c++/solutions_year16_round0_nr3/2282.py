#include<bits/stdc++.h>
using namespace std;
int n,k,a[50];
int cnt=0;
void permu(int state)
{
    int i;
    if(state==n)
    {
        if(cnt==k)return ;
        //cout<<cnt<<' ';
        cout<<"11";
        for(i=0;i<n;i++)
        {
            if(a[i]==1)cout<<"11";
            else cout<<"00";
        }
        cout<<"11";
        cout<<' ';
        for(i=3;i<=11;i++)
            cout<<i<<' ';
        cout<<endl;
        cnt++;
    }
    else
    {
        a[state]=1;
        permu(state+1);
        a[state]=0;
        permu(state+1);
    }
}
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("out4.txt","w",stdout);
    cin>>n>>n>>k;
    cout<<"Case #1:"<<endl;
    n/=2;
    n-=2;
    permu(0);
}
