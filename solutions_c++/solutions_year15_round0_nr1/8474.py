#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("output.txt","w",stdout);
    freopen("A-large.in","r",stdin);
    ios::sync_with_stdio(false);
    cin.tie(0);
    short test, i, j;
    int s, sum, req;
    cin >> test;
    for(j = 1; j <= test; j++)
    {
        cin >> s;
        char str[s+1];
        cin >> str;
        sum = 0;
        req = 0;
        for(i = 0; i < s; i++)
        {
            sum += str[i] - '0';
            if(sum < i + 1)
            {
                req += 1;
                sum += 1;
            }
        }
        cout << "Case #" << j << ": " << req  << "\n";
    }
    return 0;
}
