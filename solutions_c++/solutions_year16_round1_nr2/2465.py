#include <bits/stdc++.h>

using namespace std;

typedef pair<int,int> pii;
typedef long long ll;

#define pb push_back
#define pf push_front
#define mp make_pair
#define sz(a) (int)a.size()
#define i128 __int128
#define INF 0x3f3f3f3f
// LLONG_MIN LLONG_MaX INT_MIN INT_MaX



int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int n;
    cin >> n;
    for(int TC=1; TC<=n; TC++){
        int cnt[500] = {0};
        int m;
        cin >> m;
        for(int i=0; i<2*m-1; i++){
            for(int j=0; j<m; j++){
                int x;
                cin >> x;
                cnt[x]++;
            }
        }
        cout << "Case #" << TC << ": " ;
        for(int i=1; i<500; i++){
            if(cnt[i] != 0 && cnt[i] % 2 == 1)
                cout << i << " ";
        }
        cout << endl;
    }
    return 0;
}