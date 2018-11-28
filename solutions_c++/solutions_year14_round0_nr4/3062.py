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
#define MAX 1001

int main(){
    int t, cases = 0;
    double naomi[MAX], ken[MAX];
    cin >> t;
    while (t--){
        int n;
        cin >> n;
        for (int i = 0; i < n; i++)
            cin >> naomi[i];
        for (int i = 0; i < n; i++)
            cin >> ken[i];
        sort(naomi, naomi+n);
        sort(ken, ken+n);
        int ans1 = 0, ans2 = 0;
        int j = 0, k = 0;
        for (int i = 0; i < n; i++){
            if (naomi[i] > ken[j]){
                ans1++;
                j++;
            }
            if (ken[i] > naomi[k]){
                ans2++;
                k++;
            }
        }
        cout << "Case #" << ++cases << ": " << ans1 << " " << n-ans2 << endl;
    }
    return 0;
}
