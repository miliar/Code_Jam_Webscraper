#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define MAX 1000000
#define vi vector<int>

ll _sieve_size;
bitset<10000010> bs;
vi primes;
void sieve(ll upperbound)
{
    _sieve_size = upperbound + 1;
    bs.set();
    bs[0] = bs[1] = 0;
    for (ll i = 2; i <= _sieve_size; i++) if (bs[i])
        {
            for (ll j = i * i; j <= _sieve_size; j += i) bs[j] = 0;
            primes.push_back((int)i);
        }
}
bool isPrime(ll N)
{
    if (N <= _sieve_size) return bs[N];
    for (int i = 0; i < (int)primes.size(); i++)
        if (N % primes[i] == 0) return false;
    return true;
}
vector<ll>prime_sum;
bool check(vector<int>v)
{
    reverse(v.begin(),v.end());
    prime_sum.clear();
    for(int base=2; base<=10; base++)
    {
        ll sum=0;
        for(int i=0; i<v.size(); i++)
        {
            sum+=(pow(base,i)*v[i]);
        }
        if(isPrime(sum))
            return false;
        else
            prime_sum.push_back(sum);
    }
    return true;
}
vector<int>b,rev;
void print(vector<int>v)
{
    for(int i=0; i<v.size(); i++)
        cout<<v[i];
    cout<< " ";
    for(int i=0; i<prime_sum.size(); i++)
    {
        for(int j=0; j<primes.size() ; j++)
            if(prime_sum[i]%primes[j]==0 && prime_sum[i]!=primes[j])
            {
                cout<<primes[j]<< " ";
                break;
            }
    }
    cout<<endl;
}
int bin(int n,int c)
{
    b.clear();
    rev.clear();
    b.push_back(1);
    while(c)
    {
        int rem=n%2;
        rev.push_back(rem);
        n/=2;
        c--;
    }
    for(int i=rev.size()-1; i>=0; i--)
        b.push_back(rev[i]);
    b.push_back(1);
    if(check(b))
        return 1;
    else
        return 0;
}
int main()
{
    sieve(10000000);
    int t,n,j,c;
    FILE *f=freopen("output.txt","w",stdout);
    FILE *in=freopen("input.txt","r",stdin);
    scanf("%d",&t);
    for(ll tc=1; tc<=t; tc++)
    {
        cin>>n>>j;
        int counter=n-2;
        cout<< "Case #"<<tc<< ":\n";
        for(int i=1; i<=pow(2,counter)&& j; i++)
        {
            int ans=bin(i,counter);
            if(ans)
            {
                //j--;
                print(b);
                j--;
            }
        }
    }
    fclose(in);
    fclose(f);
    return 0;
}
