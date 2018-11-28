#include <strstream>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <string>
#include <cstdio>

#define f(i,beg,end) for(int i=beg; i<=end; i++)

using namespace std;

void redirect()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
}

int a, b;

void init()
{
    cin >> a >> b;
}

bool palindrome(int number)
{   
    string h = "";
    
    while (number)
    {
        h += (char)('0' + number%10);
        number/=10;
    }
    string revh(h.rbegin(),h.rend());
    
    return (h==revh);
}

void solve(int testnum)
{
    int ans = 0;
    
    f(i,a,b)
    {
        int x = (int) (sqrt(i));
        if (x*x!=i) continue;
        
        if (palindrome(x) && palindrome(i)) ans++;
    }
    
    cout << "Case #" << testnum << ": " << ans << endl;
}

int main()
{
    redirect();
    
    int tests = 1;   cin >> tests;
    
    f(i,1,tests)
    {
        init();
        solve(i);
    }
    
    return 0;
}