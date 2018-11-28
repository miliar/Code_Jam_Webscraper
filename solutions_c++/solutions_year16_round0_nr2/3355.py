#include <iostream>

using namespace std;

int solve(string inp)
{
    int sz = inp.size(),ans = 0;
    for (int i=sz-1; i>=0; i--) {
        if (inp[i] =='-') {
            ans++;
            for (int j=0; j<i; j++) {
                if (inp[j] == '-') {
                    inp[j] = '+';
                }
                else
                {
                    inp[j] = '-';
                }
            }
        }
    }
    return ans;
}

int main()
{
    std::ios::sync_with_stdio(false);
    int t,T;
    cin >> T;
    for (t=0; t<T; t++)
    {
        string inp;
        cin >> inp;
        int ans = solve(inp);
        cout <<"Case #"<<t+1<<": "<< ans <<endl;
    }
    return 0;
}

