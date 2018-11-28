#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <climits>
#include <queue>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <stack>
#include <map>
#include <cstring>
#include <cmath>
using namespace std;

//trocar para 0 para desabilitar output
#if 1
#define DEBUG(x) cout << x << endl
#define PAUSE() cin.get(); cin.get()
#else
#define DEBUG(x)
#define PAUSE()
#endif

#define TRACE(x) DEBUG(#x << " = " << x)
#define DEBUGS() DEBUG("***************************")
#define MAX 10001

int discs[MAX];

int main(){
    int cases = 0, t, n, x;
    cin >> t;
    while (t--){
        cin >> n >> x;
        for (int i = 0; i < n; i++){
            cin >> discs[i];
        }
        sort(discs, discs+n);
        int ans = 0;
        int low = 0, high = n-1;
        while (low <= high){
            if (discs[low]+discs[high] <= x)
                low++;
            high--;
            ans++;
        }
        cout << "Case #" << ++cases << ": " << ans << endl;
    }
    return 0;
}
