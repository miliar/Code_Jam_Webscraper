#include<bits/stdc++.h>
#define ll long long
using namespace std;
ll i=0,j,k,l,m,n,T,t=1,f=0,ans,trial;
int a[10];
bool check()
{
    for(i=0;i<10;i++)
    {
        if(a[i]==0)
        {
            return false;
        }

    }
    return true;

}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("ggl.out","w",stdout);
    cin >> T;
    while(T--)
    {
       k=2;
        cin >>n;
        if(n==0)
        {

             cout <<"Case #" <<t<<": " <<"INSOMNIA" <<endl;
             t++;
        }
        else{
        ans=n;
       while(f==0)
        {

        while(n>0)
        {
            l=n%10;
            a[l]++;


            n=n/10;

        }
        f=check();
        if(f==1)
        {   //Case #1: INSOMNIA
            cout <<"Case #" <<t<<": " <<trial <<endl;

        }
        else{
            n=ans*k;
            trial=n;
            k++;
        }
       }
       f=0;
       t++;
       memset(a,0,sizeof(a));
        }

    }

    return 0;
}
