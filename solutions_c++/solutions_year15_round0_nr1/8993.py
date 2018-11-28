#include <iostream>
#include<cstdlib>
#include<cstdio>
using namespace std;

int main()
{
    //freopen("D:\\Programming\\CodeJamQualification1\\a.txt", "r", stdin);
    //freopen("D:\\Programming\\CodeJamQualification1\\aOut.txt", "w", stdout);
    int TC;
    string s;
    cin >> TC;
    int p = 1;
    while(TC--)
    {
        int k;
        cin >> k;
        cin >> s;

        int ans = 0;
        int curr = 0;
        int arr[k+1];
        for(int i = 0; i <= k; i++)
        {
            arr[i] = s[i]-'0';
        }
        if(arr[0] == 0)
        {
            ans++;
            curr++;
        }
        else
        {
            curr += arr[0];
        }
        for(int i = 1; i <= k; i++)
        {
            if(arr[i] > 0 && curr < i)
            {
                int d = i - curr;
                curr += d;
                ans += d;
            }
            curr += arr[i];
        }


        cout << "Case #" << p << ": " << ans << endl;
        p++;
    }
    return 0;
}
