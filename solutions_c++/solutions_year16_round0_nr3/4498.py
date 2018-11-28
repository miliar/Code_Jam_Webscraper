#include<bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define ll long long
using namespace std;
ll x,M=10000000,z,k,n,t,c=1,sev;
vector<int>prime;
bool not_prime[10000000];
bool isprime(ll x);
void seive();
map<ll,bool>bs;
ll power(ll x,ll y)
{
    ll num=1;
    while(y--)  num*=x;
    return num;
}
ll toD(string s,ll x)
{
    ll ans=0;
    for(int i=s.size()-1,j=0 ; i>=0 ; i--,j++)
        if(s[i]=='1')
        {
            ans+=(ll)power(x,j);
        }
    return ans;
}
void Val(string s)
{
    ll arr[11];
    for(int i=2 ; i<=10 ; i++)
        arr[i]=toD(s,i);
    //for(int i=2 ; i<=10 ; i++)  cout<<arr[i]<<" ";cout<<endl;
    bool M=1;
    for(int i=2 ; i<=10 ; i++)
            if(isprime(arr[i]))  M=0;
    if(M)
    {
            //for(int i=2 ; i<=10 ; i++)  cout<<arr[i]<<" ";cout<<endl;
            k--;
            cout<<s<<" ";
            for(int i=2 ; i<=10 ; i++)
            {
               int sz=sqrt(arr[i])+1;
               for(int j=2 ; j<=sz ; j++)
                    if(arr[i]%j==0)
                    {
                        cout<<j<<" ";
                        break;
                    }
            }
            cout<<endl;
       }
}
void gen(string s,int G)
{
    if(!k)  return;
    if(G==s.size())
    {
        s="1"+s+"1";
        Val(s);
        return;
    }
    gen(s+'1',G);
    gen(s+'0',G);
}
int main(){
    //cout<<toD("111111",10)<<endl;
    seive();
    freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
    cin>>t;
    while(t--)
    {
        cin>>n>>k;
        cout<<"Case #"<<c++<<":"<<endl;
        gen("",n-2);
    }


}
void seive()
{
    sev=1000000;
	not_prime[0]=1;
	not_prime[1]=1;
	for(int i=2 ; i*i<=M ; i++)
	{
		if(!not_prime[i])
        {
			for(int j=i*2 ; j<M ; j+=i)
				not_prime[j]=1;
			prime.pb(i);
        }
	}
}
bool isprime(ll x)
{
    if(x<sev)
        return (!not_prime[x]);
    for(int i=0 ; i<prime.size() ; i++)
    {
        if(x%prime[i]==0)   return 0;
    }
    return 1;
}
