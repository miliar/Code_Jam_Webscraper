#include<bits/stdc++.h>
using namespace std;
int hash[10],cnt;

void getdigit(int x)
{
    while(x!=0)
    {
        int d=x%10;
        if(hash[d]==0)
        {
            cnt++;hash[d]=1;
        }
        x=x/10;
    }
}

int main()
{
    int t,i,j,it,n;
    cin>>t;
    for(it=1;it<=t;it++)
    {
        cin>>n;
        cout<<"Case #"<<it<<": ";
        if(n==0)
        {cout<<"INSOMNIA\n";continue;}
        for(i=0;i<10;i++)
            hash[i]=0;
        int nn=0;
        cnt=0;
        while(cnt!=10)
        {
            nn+=n;
            getdigit(nn);
        }
        cout<<nn<<endl;
    }
    return 0;
}
