#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
typedef long long ll;

int digits(int x)
{
    int n=0;
    while(x>0)
    {
        x = x/10;
        n++;
    }
    return n;
}

bool isPal(ll x)
{
    vector<int> str;
    while(x>0)
    {
        str.push_back(x%10);
        x /= 10;
    }
    int len = str.size();
    for(int i=0;i<len/2;i++)
    {
        if(str[i]!=str[len-1-i])
            return false;
    }
    return true;
}

void gen(int x, int& x1, int & x2)
{
    int xc = x;
    x2 = x;
    while(xc>0)
    {
        int d = xc%10;
        x2 = x2*10 + d;
        xc = xc/10;
    }

    xc = x;
    x1 = x;
    xc /= 10;
    while(xc>0)
    {
        int d = xc%10;
        x1 = x1*10 + d;
        xc = xc/10;
    }
}

vector<ll> count(ll A, ll B)
{
    vector<ll> all;
    int lb = (int)ceil(sqrt((double)A));
    int ub = (int)floor(sqrt((double)B));
    
    int ld = (digits(lb)+1)/2;
    int ud = (digits(ub)+1)/2;

    int s = 1;
    while(ld>1){
        s*=10;
        ld--;
    }
    int e = 9;
    while(ud>1) {
        e = e*10+9;
        ud--;
    }

    for(int i=s;i<=e;i++)
    {
        int p1, p2;
        gen(i, p1, p2);
        ll p12 = p1*1LL*p1;
        if(p12 >=A && p12 <= B && isPal(p12))
        {
            all.push_back(p12);
        }
        ll p22 = p2*1LL*p2;
        if(p22 >=A && p22 <= B && isPal(p22))
        {
            all.push_back(p22);
        }
    }

    return all;
}

int main()
{
    freopen("fairsquare.in", "r", stdin);
    freopen("fairsquare.out", "w", stdout);

    ll A, B;
    A = 1;
    B = 100000000000000;
    vector<ll> all = count(A, B);
    sort(all.begin(), all.end());
    //for(int i=0;i<all.size();i++)
    //{
    //    cout << all[i] << " ";
    //}
    //cout << endl;

    int T;
    cin >> T;
    for(int t=0;t<T;t++)
    {
        cin >> A >> B;
        int res = 0;
        for(int i=0;i<all.size();i++)
        {
            if(all[i]>=A && all[i]<=B)
                res++;            
        }
        cout << "Case #" << t+1 <<": " << res << endl;
    }
    return 0;
}
