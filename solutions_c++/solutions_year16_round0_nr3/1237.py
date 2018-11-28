#include<bits/stdc++.h>
#define ll long long int
#define inf 1000000000
#define mod 1073741824
using namespace std;

void rec(ll i);
ll n,arr[16],want,ctr;
int main()
{
    ll t,j;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    cin>>t>>n>>j;
    want=j;
    ctr=0;
    cout<<"Case #1:"<<endl;
    rec(0);

    return 0;
}

void rec(ll i)
{
    ll j,k,l,no,flag,brr[12];
    if(i==n)
    {
        if(arr[n-1]==0)
            return ;
        if(ctr==want)
            return;
        for(j=2;j<=10;j++)
        {
            l = 1;
            no = 0;
            for(k=15;k>=0;k--)
            {
                no += arr[k] * l;
                l *= j;
            }

            flag=1;
            for(k=2;k<=sqrtl(no);k++)
            {
                if(no%k == 0)
                {
                    brr[j] = k;
                    flag=0;
                    break;
                }
            }
            if(flag==1)
                return;
        }

        for(j=0;j<16;j++)
            cout<<arr[j];
        cout<<" ";
        for(j=2;j<=10;j++)
            cout<<brr[j]<<" ";
        cout<<endl;
        ctr++;
        return;

    }

    arr[i] = 1;
    rec(i+1);
    if(ctr==want)
        return;
    arr[i] =0;
    rec(i+1);

}
