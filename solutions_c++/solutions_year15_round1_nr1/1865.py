#include <fstream>

using namespace std;

const int MAXN = 1<<10;

int T;
int n, a[MAXN];

int main(){
    ifstream cin("C:\\Users\\USER\\Downloads\\A-large.in");
    ofstream cout("Al.out");
    cin >> T;
    for(int t = 1; t <= T; t++){
        cout << "Case #" << t << ": ";
        cin >> n;
        for(int i = 0; i < n; i++) cin >> a[i];
        int y = 0;
        for(int i = 1; i < n; i++)
            if(a[i] < a[i-1]) y += (a[i-1]-a[i]);
        int mx = 0, z = 0;
        for(int i = 1; i < n; i++)
            mx = max(mx, a[i-1]-a[i]);
        for(int i = 0; i < n-1; i++)
            z += min(a[i], mx);
        cout << y << ' ' << z << '\n';
    }
    return 0;
}
