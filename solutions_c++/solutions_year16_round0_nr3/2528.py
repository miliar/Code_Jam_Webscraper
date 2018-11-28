#include <bits/stdc++.h>

#define mod 1000000007
#define inf 1000000000000
#define root2 1.41421
#define root3 1.73205
#define pi 3.14159
#define MAX 10000001
#define ll long long int
#define ss(n) scanf("%lld", &n)
#define ssf(n) scanf("%lf", &n)
#define gc getchar
#define pb push_back
using namespace std;
ll base[9];
ll checkPrime(ll num)
{
    ll i, j;
    for(i=2;i*i<=num;i++)
        if(num%i==0)
            return i;
    return -1;
}
ll convertToBinary(ll num)
{
    if(num==1||num==0)
        return num;
    return convertToBinary(num/2)*10+num%2;
}
ll nextNum(ll z)
{
    ll n=z+2, cnt=0;
    return convertToBinary(n);
}

int main()
{
    ifstream in("C-small-attempt0.in");
    ofstream out("output.txt");
    ll t, i, k, j=1, n, m, num, z, div[9], found, cnt=0, a;
    in>>t;
    while(j<=t)
    {
        out<<"Case #"<<j<<":\n";
        in>>n>>m;
        num=1000000000000001;
        while(cnt!=m)
        {
            found=true;
            for(i=2;i<11;i++)
            {
                base[i-2]=0;
                z=num;
                a=1;
                while(z)
                {
                    base[i-2]=base[i-2]+(z%10)*a;
                    a=a*i;
                    z/=10;
                }
                div[i-2]=checkPrime(base[i-2]);
                if(div[i-2]==-1)
                {
                    found=false;
                    break;
                }
            }
            n=num;z=0;a=1;
            while(n)
            {
                z=z+(n%10)*a;
                a*=2;
                n/=10;
            }
            n=num;
            num=nextNum(z);
            if(!found)
            {
                continue;
            }
            out<<n<<" ";
            for(i=0;i<8;i++)
                out<< div[i] << " ";
            out<<div[8]<<endl;
            cnt++;
        }
        j++;
    }
}
