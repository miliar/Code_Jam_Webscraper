#include <iostream>
#include <cstdlib>

using namespace std;

void Calc(int r, int t, int i);

int main() {
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    
    int T;
    int r, t;
    cin >> T;
    for(int i=1; i<=T; i++){
        cin >> r >> t;
        Calc(r, t, i);
    }

    return 0;
}

void Calc(int r, int t, int i){
    int temp = 0;
    int n1 = (r + 1) * (r + 1) - r * r;
    temp += n1;
    int ans = 1;

    while(temp < t){
        n1 += 4;
        temp += n1;
        ans++;
    }

    ans = (temp == t) ? ans : ans-1;

    cout << "Case #" << i << ": " << ans << endl;
}
