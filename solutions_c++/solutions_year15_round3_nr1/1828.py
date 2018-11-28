#include <iostream>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    int r, c, w, ans;
    for(int i=0;i<t;++i) {
        cin >> r >> c >> w;
        if(c%w==0)
            ans = (c/w)+w-1;
        else
            ans = (c/w)+w;
        cout << "Case #" << i+1 << ": " << ans << '\n';
    }
    return 0;
}
