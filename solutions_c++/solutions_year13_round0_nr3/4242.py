#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int checkFairLong(const long long int &n)
{
    long long int k = n;
    vector<int> digits;
    while(k > 0)
    {
        long long int q = k/10LL;
        long long int r = k - q*10LL;
        digits.push_back((int)r);
        k = (k - r)/10LL;
    }
    size_t s = digits.size();
    if(digits.size() == 1) return 1;
    size_t s2 = s;
    if(s&1) s++;
    s = s>>1;
    for(size_t i = 0; i < s; ++i)
    {
        if(digits[i] != digits[s2-i-1]) return 0;        
    }
    return 1;
}

int checkFairInt(const int &n)
{
    int k = n;
    vector<int> digits;
    while(k > 0)
    {
        int q = k/10;
        int r = k - q*10;
        digits.push_back(r);
        k = (k - r)/10;
    }
    size_t s = digits.size();
    if(digits.size() == 1) return 1;
    size_t s2 = s;
    if(s&1) s++;
    s = s>>1;
    for(size_t i = 0; i < s; ++i)
    {
        if(digits[i] != digits[s2-i-1]) return 0;        
    }
    return 1;
}

int main(int argc, char* argv[])
{
    int T; cin >> T;
    vector<long long int> fs;
    for(int n = 1; n <= 10000000; ++n)
    {
        if(checkFairInt(n) == 1)
        {
            long long int N = (long long int)n*(long long int)n;
            if(checkFairLong(N) == 1)
            {
                fs.push_back(N);
            }
        }
    }
    for(int i = 0 ; i < T; ++i)
    {
        long long int a; cin >> a; 
        long long int b; cin >> b;
        int ans = 0;
        for(vector<long long int>::iterator z = fs.begin(); z != fs.end(); ++z)
        {
            if(((*z) >= a) && ((*z) <= b)) ans++;
        }
        cout << "Case #" << (i+1) << ": " << ans << endl;
    }
	return 0;
}

