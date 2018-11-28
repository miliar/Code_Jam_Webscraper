#include<algorithm>
#include<string>
#include<vector>
#include<iostream>

using namespace std;

int main(void)
{
    int test;
    cin >> test;
    for(int j = 1; j <= test; j++)
    {
        int len;
        cin >> len;
        string str;
        cin >> str;
        int stand = 0;
        int ans = 0;
        for(int i = 0; i < len; i++)
        {
            int temp = str[i] - '0';
            stand += temp;
            if(stand >= len) break;
            if(stand < i+1)
            {
                stand++;
                ans++;
            }
        }

        cout << "Case #" << j << ": " << ans << endl;
    }

    return 0;
}
