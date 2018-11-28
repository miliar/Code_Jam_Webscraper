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
#define MAX 16

int r1[MAX], r2[MAX];

int main(){
    int t, cases = 0;
    cin >> t;
    while (t--){
        int n1, n2;
        cin >> n1;
        for (int i = 0; i < MAX; i++){
            int aux;
            cin >> aux;
            r1[aux-1] = i / 4;
        }
        cin >> n2;
        for (int i = 0; i < MAX; i++){
            int aux;
            cin >> aux;
            r2[aux-1] = i / 4;
        }
        n1--; n2--;
        int ans = -1;
        for (int i = 0; i < MAX; i++){
            if (r1[i] == n1 && r2[i] == n2){
                if (ans == -1) ans = i;
                else ans = -2;
            }
        }
        cout << "Case #" << ++cases << ": ";
        if (ans == -1) cout << "Volunteer cheated!" << endl;
        else if (ans == -2) cout << "Bad magician!" << endl;
        else cout << ans+1 << endl;
    }
    return 0;
}
