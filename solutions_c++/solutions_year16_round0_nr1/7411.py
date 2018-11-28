# include <iostream>
# include <cstring>
# include <algorithm>
using namespace std;
# define endl '\n'
# define ll long long
# define mod 1000000007
ll int t,tt,n,m;
int a[10];
bool fun()
{
    ll temp = m;
    bool mark=0;
    while(temp)
    {
        if(!a[temp%10])
            a[temp%10]=1;
        temp/=10;
    }
    for(int i=0;i<10;++i)
        if(!a[i]) mark = 1;
    if(mark==1)return 0;
    return 1;
}
int main ()
{
    cin>>t;
    for(tt=0;tt<t;++tt)
    {
        cin>>n;
        if(n==0)cout<<"Case #"<<tt+1<<": INSOMNIA\n";
        else
        {
            memset(a,0,sizeof(a));
            m=n;
            while(!fun())
            {
                m+=n;
            }
            cout<<"Case #"<<tt+1<<": "<<m<<endl;
        }
    }
    return 0;
}
