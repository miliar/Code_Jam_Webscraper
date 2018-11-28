#include <bits/stdc++.h>
using namespace std;
int n;
bool z[10]={0};
bool check()
{
    for(int i=0;i<10;i++)
        if(z[i]==false)
        return false;
    return true;
}
void Clear()
{
    for(int i=0;i<10;i++)
        z[i]=false;
}
void solve(int testCase,int n)
{
    if(n==0)
    {
        cout<<"Case #"<<testCase<<": INSOMNIA"<<endl;
        return ;
    }
    int Z=n,i;
    for( i=1;;i++)
    {
     n=i*Z;
    while(n>0)
    {
        z[n%10]=true;
        n/=10;
    }
    if(check()){
        cout<<"Case #"<<testCase<<": "<<Z*i<<endl;
        break;
    }

    //cout<<"checking at "<<n<<endl;
    }

}

int main()
{
int t;
cin>>t;
for(int i=1;i<=t;i++)
{
        Clear();
    cin>>n;
    solve(i,n);

}
    return 0;
}
// ????? ?????
