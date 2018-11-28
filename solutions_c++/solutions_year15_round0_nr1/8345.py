#include <iostream>
#include <algorithm>
#include <cstdio>
#include <climits>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <stack>
#include <queue>
using namespace std;
#define si(n) scanf("%d",&n)
#define sf(n) scanf("%f",&n)
#define sl(n) scanf("%lld",&n)
#define lld long long
#define ld long double
#define pb push_back 
#define MOD 1000000007
#define PI 3.14159265
lld modpow(lld a,lld n,lld temp){lld res=1,y=a;while(n>0){if(n&1)res=(res*y)%temp;y=(y*y)%temp;n/=2;}return res%temp;}
long long mul_inv(long long  a, long long b)
{
    return modpow(a,b-2,b);
}


int main()
{
    int t;

    long long n,i;
    cin >> t;
    int count=1;
    while(t--)
    {
        cin >> n;
        string s;
        cin >> s;
        long long sh=0,p=0;
        long long ans=0;
        
        for(i=0;i<=n;i++)
        {
            int val = s[i]-'0';
            
            if(p<i)
            {
                //cout << i << ' ' << p <<endl;
                ans+=i-p;
                p=i;
            }
            p+=val;
            
        }
        cout << "Case #" << count <<": " << ans <<endl;
        count++;
    }

    return 0;
}
