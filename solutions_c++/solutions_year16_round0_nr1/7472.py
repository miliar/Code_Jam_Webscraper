//Copyright of code reserved with Arpit Bajaj
//Date : 09-04-2016
#include<bits/stdc++.h>
#define pii pair<int,int>
#define ll long long
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define ll long long
#define debug(x) cout<<">value ("<<#x<<") : "<<x<<endl;
#define MOD 1000000007
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
        cin.tie(NULL);
    freopen("large.in","r",stdin);
    freopen("outlarge.txt","w",stdout);
    int test,t;
    cin>>test;
    for(t=1;t<=test;t++)
    {
        ll n,i,j;
        cin>>n;
        bool A[10];
        for(i=0;i<10;i++)
            A[i]=0;
        ll temp1 = n,temp2=n;
        while(temp1)
        {
            int dig = temp1%10;
            A[dig]=true;
            temp1/=10;
        }
        for(j=0;j<10;j++)
        {
            if(A[j]==false)
                break;
        }
        if(j==10)
        {
            cout<<"Case #"<<t<<": "<<temp2<<endl;
            continue;
        }
        for(i=2;i<=100000;i++)
        {
            temp2+=n;
            temp1=temp2;
            while(temp1)
            {
                int dig = temp1%10;
                A[dig]=true;
                temp1/=10;
            }
            for(j=0;j<10;j++)
            {
                if(A[j]==false)
                    break;
            }
            if(j==10)
            {
                cout<<"Case #"<<t<<": "<<temp2<<endl;
                break;
            }
        }
        if(i>100000)
            cout<<"Case #"<<t<<": INSOMNIA"<<endl;
    }
    return 0;
}
