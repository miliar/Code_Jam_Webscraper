#include <iostream>
#include <stdio.h>

using namespace std;

int solve(string s)
{
    int ans = 0 ;
    bool state ;
    s[0] == '-' ? state = false : state = true ;
    for(int i = 1 ; i < s.size() ;i++)
    {
        if(s[i-1]!=s[i])
        {
            ans++ ;
            state = !state ;
        }
    }
    if(state ==  false)
        ans ++ ;
    return ans ;
}

int main()
{
    freopen("input2.in","r",stdin);
    freopen("output2.out","w",stdout);
    int test ;
    int ans ;
    string s ;
    cin >> test ;
    for(int i = 1 ; i <= test ; i++)
    {
        cin >> s ;
        ans = solve(s);
        cout << "Case #"<<i <<": " << ans << endl ;
    }
    return 0;
}
