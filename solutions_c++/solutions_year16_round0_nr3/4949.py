#include <iostream>
#include <sstream>
#include <string>

using namespace std;

const int maxl = (2<<18);
bool is_prime[maxl];
long long int divi[maxl];
int n, j;
long long int divt;
string rep(int x)
{
    string ans = "";
    for (int i=n-1; i>= 0; --i)
        if ( (1<<i) & x) 
            ans += '1';
        else
            ans += '0';
    return ans;
}

bool prime(long long int x)
{
    if (x < maxl) {
        divt = divi[x];
        return is_prime[x];
    }
    for (long long int i = 2; i * i <= x; ++i)
        if (x % i == 0) {
            divt = i;
            return false;
        }
    return true;
}
long long int in_base(int x, int base)
{
    long long int  ans = 0;
    long long int  i = 1;
    while(x) {
        if (x%2)
            ans += i;
        i *= base;
        x/=2;
    }
    return ans;
}

bool is_jam(int x)
{
    stringstream ans;
    ans << rep(x) << " ";
    for (int i=2; i < 11; ++i) {
        long long int c = in_base(x, i);
        if (prime(c))
            return false;
        else 
            ans << divt<< " " ;
    }
    cout << ans.str()<<endl;
    return true;
}
int main()
{
    fill(is_prime, is_prime+maxl, true);
    is_prime[0]=is_prime[1]=0;
    for (int i = 2; i < maxl; ++i) {
        if (is_prime[i]) {
            for (int k = 2; i*k < maxl; ++k) {
                is_prime[i*k]=false;
                divi[k*i]=i;
            }
        }
    }
    int t; cin>>t;
    cin>>n>>j;
    cout << "Case #1:"<<endl;
    int count = 0;
    for (int i = (1<<(n-1))+1; i < (1<<n); i+=2) {
        if (count < j && is_jam(i))
            count++;
        if (count==j)
            break;
    }
    return 0;
}
