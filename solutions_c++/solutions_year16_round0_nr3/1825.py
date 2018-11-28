#include<bits/stdc++.h>
using namespace std;
# define ll long long
ll slow_factorise(ll n)
{
    if(n<=2)
        return 0;
    if(n%2==0)
        return 2;
    for(ll i=3;i<=sqrt(n);i+=2)
        if(n%i==0)
        return i;
    return 0;
}
int main()
{
  //  ifstream cin("a.txt");
    ofstream cout("b.txt");
    int t,n,j,tc=0;
    cin>>t;
    while(t--)
    {
        tc++;
        cout<<"Case #"<<tc<<":\n";
        cin>>n>>j;
        int ar[n];
        int cs=pow(2,n);
        int tmp=0;
        while(tmp<cs)
        {
            for(int i=1;i<=n;i++)
                ar[i]=0;
            int temp=tmp++;
            int k=n;
            while(temp)
                ar[k--]=temp%2,temp>>=1;
            vector <ll> v;
            if(ar[1]==ar[n] && ar[1]==1)
            {
            for(ll i=2;i<=10;i++)
            {
                ll put=0;
                for(int k=1;k<=n;k++)
                    put=(put*i)+ar[k];
                v.push_back(slow_factorise(put));
            }
            bool cond=true;
            for(int i=0;i<v.size() && cond ;i++)
                if(v[i]==0)
                cond=false;
            if(cond)
            {
                j--;
                for(int i=1;i<=n;i++)
                    cout<<ar[i];
                cout<<" ";
                for(int i=0;i<v.size();i++)
                    cout<<v[i]<<" ";
                cout<<endl;
            }
            }
            if(j==0)
                break;
        }
    }
}
