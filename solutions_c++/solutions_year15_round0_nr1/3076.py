#include <bits/stdc++.h>
using namespace std;
int shyness[10005];
int main(){
    freopen("standingovation.in", "r", stdin);
    freopen("standingovation.out", "w", stdout);
    int i, j, k, t, n, Case=1;
    char ch;
    cin >> t;
    while(t--){
        cin >> n;
        for(i=0;i<=n;i++){
            cin >> ch;
            shyness[i] = ch-48;
        }
        int cnt=0, sum=0;

        for(i=1;i<=n;i++){
            sum+=shyness[i-1];
            if(sum<i) cnt+=(i-sum), sum = i;
        }
        cout << "Case #" << Case++ << ": " << cnt << endl;
    }

return 0;

}
