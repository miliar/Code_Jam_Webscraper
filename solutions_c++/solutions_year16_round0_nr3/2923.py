# include <string> 
# include <vector> 
# include <iostream> 
# include <sstream> 
# include <cstdio> 
# include <cstdlib> 
# include <cmath> 
# include <cctype> 
# include <cstring> 
# include <map> 
# include <queue> 
# include <deque> 
# include <set> 
# include <algorithm> 
# include <utility> 
# include <functional> 
# include <stack> 
# include <bitset> 
# include <complex> 
# include <cassert> 
# include <ctime> 
# include <list> 
# include <valarray> 

using namespace std;

typedef long long ll;

bool is_prime(ll n)
{
    for(ll i = 2; i  * i <= n; i++)
    {
        if(n % i == 0)
            return false;
    }
    return true;
}

ll get_divisor(ll n)
{
    for(ll i = 2; i  * i <= n; i++)
    {
        if(n % i == 0)
            return i;
    }
    return -1;
}

ll convert_to_base(ll s, ll b)
{
    ll mult = 1;
    
    ll res = 0;
    
    while(s != 0)
    {
        if((s & 1) == 1)
            res += mult;
            
        mult *= b;
        s = s >> 1;
    }
    
     return res;
}

string print_num(ll s)
{
    string str = "";
    while(s != 0)
    {
        if((s & 1) == 1)
            str.append("1");
        else str.append("0");
        
        s = s >> 1;
    }
    return string(str.rbegin(), str.rend());
}

void work(ll N, ll J)
{
    ll s = (1 << (N-1)) + 1;
    
    ll count = 0;
    for(; s <= (1 << N); s++)
    {
        if(count == J)
            return;
            
        // first digit is not one, continue;
        if(s % 2 == 0)
            continue;
        
        bool ok = true;
        vector<ll> divisors;
        for(ll b = 2; b <= 10; b++)
        {
            ll num = convert_to_base(s, b);
            
            if(is_prime(num))
            {
                ok = false;
                break;
            }
            else divisors.push_back(get_divisor(num));
        }
        
        if(ok)
        {
            cout << print_num(s);
            for(ll i = 0; i < divisors.size(); i++)
                cout << " " << divisors[i];
            cout << endl;
            
            count++;
        }
    }
}

int main()
{
	ll t;
    cin >> t;
    
    ll N, J;
    cin >> N >> J;
    
    cout << "Case #1:" << endl;
    work(N,J);
	return 0;
}

