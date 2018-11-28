#include <iostream>
#include <vector>
using namespace std;

int main() {
    int t; cin >> t;
    for (int cas=1; cas<=t;++cas) {
        cout << "Case #" << cas << ": ";
        int a,b,x;
        int f[17];
        for (int i=0;i<17;++i) f[i]=0;
        cin >> a; --a;
        for (int i=0;i<4;++i) for (int j=0;j<4;++j) {
            cin >> x;
            if (i==a) f[x]++;
        }
        cin >> b; --b;
        for (int i=0;i<4;++i) for (int j=0;j<4;++j) {
            cin >> x;
            if (i==b) f[x]++;
        }
        int q = 0, ans=-1;
        for (int i=0;i<17;++i) if (f[i]==2) {
            ++q;
            ans=i;
        }
        if (q>1) cout << "Bad magician!" << endl;
        else if (q==0) cout << "Volunteer cheated!" << endl;
        else cout << ans << endl;
    }
}