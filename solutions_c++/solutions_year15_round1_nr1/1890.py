#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("file.in","r",stdin);
    freopen("file.out","w",stdout);
    int T,tc(1),n,arr[1001];
    cin >> T;
    while(T--){
        cin >> n;
        int a(0),b(0),Max(-1);
        for(int i=0;i<n;i++){
            cin >> arr[i];
            if(i && arr[i]<=arr[i-1]){
                a+= arr[i-1] - arr[i];
                Max = max(Max,arr[i-1]-arr[i]);
            }
        }
        for(int i=0;i<n-1;i++){
            b += min(arr[i],Max);
        }
        cout << "Case #" << tc++ << ": " << a << " " << b << endl;
    }
    return 0;
}
