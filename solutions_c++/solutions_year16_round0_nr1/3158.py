#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;
bool A[15];

long long count(long long n)
{
    long long x = 1, y;
    char s[20];
    bool flag = false;
    while(!flag)
    {
        y = x*n;
        sprintf(s, "%lld", y);
        for(int i = 0, l = strlen(s);i < l;++i)
            A[s[i]-'0'] = true;
        flag = true;
        for(int i = 0;i < 10;++i)
            if(A[i] == false)
            {
                flag = false;
                break;
            }
        x++;
    }
    return y;
}

int main()
{
    ios::sync_with_stdio(false);
    int t;
    long long ans = 0, n;
    cin >> t;
    for(int c = 1;c <= t;++c)
    {
        cin >> n;
        memset(A, false, sizeof(A));
        cout << "Case #" << c << ": ";
        if(n == 0)
            cout << "INSOMNIA" << endl;
        else
        {
            ans = count(n);
            cout << ans << endl;
        }
    }
    return 0;
}
