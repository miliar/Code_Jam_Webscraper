#include<iostream>
#include<cstring>

using namespace std;

int solve()
{
    int smax;
    cin >> smax;
    int arr[1002];
    string shyness;
    cin >> shyness;
    for(int i=0; i <= smax; i++) {
        arr[i] = shyness.at(i) - '0';
    }
    int ans = 0;
    int sum = arr[0];
    for(int i=1;i <= smax; i++) {
        if(arr[i] && (i > (sum + ans))) {
            ans = i - sum;
        }
        sum += arr[i];
    }
    return ans;
}

int main()
{
    int t,counter;
    cin >> t;
    for(int i=1; i <= t; i++) {
        int ans = solve();
        cout << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}
