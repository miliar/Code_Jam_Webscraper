#include <iostream>
#include <cstdio>
using namespace std;
int main() {
    //freopen("A. Standing Ovation.out","w",stdout);
    int tc;
    cin >> tc;
    for (int a=0; a<tc; a++) {
        int n,ans=0;
        string s;
        cin >> n >> s;
        int arr[n+1];
        for (int i=0; i<n+1; i++) {
            arr[i] = (int)s[i] - 48;
            if (i>0) arr[i] += arr[i-1];
        }
        for (int i=0; i<n+1; i++) {
            while(arr[i] < i+1) {
                for (int j=i; j<n+1; j++) {
                    arr[j]++;
                }
                ans++;
            }
        }

        cout << "Case #" << a+1 << ": " << ans << "\n";
    }
}
