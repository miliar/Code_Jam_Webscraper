#include <bits/stdc++.h>
#include <conio.h>
using namespace std;
int t,n,zz;
int dem=0;
bool check[10];
int expand(int n)
{
    int rep=n;
    while(n!=0)
    {
        int k=n%10;
        n/=10;
        if(check[k])
        {
            check[k]=true;
        }
        else
        {
            check[k]=true;
            dem++;
        }
        if(dem==10) return rep;
}
        if(dem!=10) return -1;
}
void solve(int t)
{
    memset(check,false,sizeof(check));
    dem=0;
    {
        long long z=t;
        while(expand(z)==-1)
        {
        //cout<<z<<" ";
        //for(int i=0;i<=9;i++) if(check[i]) cout<<i<<" ";
        //cout<<endl;
            //cout<<z<<" "<<dem<<endl;
            //getch();
            z+=t;
        }
        cout<<expand(z)<<endl;
        }
        //for(int i=0;i<=9;i++) if(check[i]) cout<<i<<" ";
}
int main()
{
    freopen("jama.in","r",stdin);
    freopen("jama.out","w",stdout);
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cin>>n;
        cout<<"Case #"<<i+1<<": ";
    if(n==0) cout<<"INSOMNIA"<<endl;
    else solve(n);}
}
