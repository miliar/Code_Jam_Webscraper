#include<bits/stdc++.h>
using namespace std;
#define MAX 1000001
typedef long long ll;
ll pp[MAX];
ll ln(ll n)
{
    ll i=1;int buc[10]={0};
    while(true)
    {
        ll t=n*i;
        while(t)
        {
            buc[t%10]=1;
            t /= 10;
        }
         i++; int sum=0;
        for(int j=0;j<10;j++)
            sum += buc[j];
        if(sum==10)
        {
            ll ans = n*(i-1);
            return ans;
        }
    }
}
int main()
{
    for(ll i=1;i<MAX;i++)
    {
        pp[i] = ln(i);
    }
    ifstream IF;
    IF.open("input.txt");
    ofstream OF;
    OF.open("output.txt");
    int t; IF >> t;
    for(int tt=1;tt<=t;tt++)
    {
        int n; IF >> n;
        if(n==0)
            OF << "Case #" << tt << ": " << "INSOMNIA" << endl;
        else
            OF << "Case #" << tt << ": " << pp[n] << endl;
    }
    OF.close(); IF.close();
}
