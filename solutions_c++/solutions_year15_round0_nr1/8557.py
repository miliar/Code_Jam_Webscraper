#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
#ifndef ONLINE_JUDGE
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
#endif
    ios_base::sync_with_stdio(0);
    int test_cases, num;
    cin >> test_cases;
    for(int test_no = 1; test_no <= test_cases; test_no++)
    {
        cout << "Case #" << test_no << ": ";
        string s;
        cin >> num >> s;
        int stand = 0, req = 0;
        for(int i = 0; i <= num; ++i)
        {
            if(s[i] == '0') continue;
            if(stand >= i)
                stand += s[i] - '0';
            else
            {
                req += i - stand;
                stand = i + s[i] - '0';
            }
        }
        cout << req << endl;
    }
}
