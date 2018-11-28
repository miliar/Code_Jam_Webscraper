#include <bits/stdc++.h>
#define fi first
#define se second
#define fastio ios::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define endl "\n"
#define mod 1000000007
#define pb push_back
#define mp make_pair
using namespace std;

int t,a[15],r;
long long n,i,j,p,k;

int check()
{
    for(int it=0;it<10;it++)
    {
        if(a[it]==0)
            return -1;
    }
    return 1;
}

int main() {
    //fastio
    freopen("A-large.in","r",stdin);
    freopen("output1.txt","w",stdout);

    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>n;
        for(j=0;j<10;j++)
            a[j]=0;
        if(n==0)
        {
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
            continue;
        }
        k=1;
        while(1)
        {
            p=k*n;
            while(p>0)
            {
                r=p%10;
                a[r]=1;
                p/=10;
            }
            if(check()==1)
            {
                long long q=k*n;
                cout<<"Case #"<<i<<": "<<q<<endl;
                break;
            }
            k++;
        }
    }
}
