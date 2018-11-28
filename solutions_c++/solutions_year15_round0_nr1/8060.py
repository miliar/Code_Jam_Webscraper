#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.out", "w", stdout);
    int t, c = 0;
    cin >> t;
    while(t--){
        int n, maxsum = 0, Max = 0, sum = 0;
        int arr[1010] = {0};
        string s;
        cin >> n >> s;
        for (int x = 0; x < s.size(); x++){
               arr[x] = s[x]-'0';
        }
        for (int x = 0; x <= n; x++){
            if(x <= sum)
               sum += arr[x];
            else{
                Max += x-sum;
                sum+= x-sum;
                sum += arr[x];
            }
        }

        cout << "Case #" << ++c << ": " << Max << endl;
    }
    return 0;
}
