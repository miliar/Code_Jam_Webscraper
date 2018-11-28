#include <iostream>
using namespace std;
int min(int a, int b){
    return a>b?b:a;
}
int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++){
        int a[1001];
        int n;
        cin >> n;
        for(int i = 1; i <= n; i++){
            cin >> a[i];
        }
        int sum1 = 0;
        int max = 0;
        for(int i = 2; i <= n; i++){
            if(a[i] < a[i - 1]){
                sum1 += a[i - 1] - a[i];
                if(a[i - 1] - a[i] > max){
                    max = a[i - 1] - a[i];
                }
            }
        }
        int sum2 = 0;
        for(int i = 1; i < n; i++){
            sum2 += min(a[i],max);
        }
        cout << "Case #" << tt << ": "<<sum1 << " " << sum2<<endl;
    }
    return 0;
}
