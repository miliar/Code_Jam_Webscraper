#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 10000000;

bool is_palindrome(long long n)
{
    long long p10 = 1;
    while(p10 <= n)
    {
	p10 *= 10;
    }
    
    p10 /= 10;
    
    while(n >= 10)
    {
	long long d = n % 10;
	if (n < d*p10 || n >= (d+1)*p10)
	{
	    return false;
	}
	
	n -= d*p10;
	n /= 10;
	p10 /= 100;
    }
    
    return true;
}

vector<long long> get_fair(int n)
{
    vector<long long> fair;
    for (long long p=1;p<=n;++p)
    {
	if (is_palindrome(p) && is_palindrome(p*p))
	{
	    fair.push_back(p*p);
	}
    }
    
    return fair;
}

long long count_fair(long long a, const vector<long long>& fair)
{
    auto it = upper_bound(fair.begin(), fair.end(), a);
    return (it - fair.begin());
}

int main()
{
    auto fair = get_fair(MAXN);
    int t;
    cin >> t;
    for(int lp=1;lp<=t;++lp)
    {
	long long a, b;
	cin >> a >> b;
	cout << "Case #" << lp << ": " << (count_fair(b, fair) - count_fair(a-1, fair)) << "\n";
    }
    
    return 0;
}