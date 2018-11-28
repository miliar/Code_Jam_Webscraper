#include <iostream>
using namespace std;
int main() {
    int t;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> t;
    for (int tt = 1; tt <= t; tt++){
        int smax, sum = 0, ans = 0;
        string st;
        cin >> smax;
        cin >> st;
        for(int i = 0; i <= smax; i++){
            int x = st[i] - '0';
            if (sum < i){
                ans += i - sum;
                sum = i + x;
            }else{
                sum += x;
            }
        }
        cout<<"Case #"<<tt<<": "<<ans<<endl;
    }
    return 0;
}
