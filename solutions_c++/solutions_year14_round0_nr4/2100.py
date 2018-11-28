#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <string>
#include <set>
#include <map>
#include <list>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <cstdio>
#include <cmath>
using namespace std;

int main()
{
    int N, T;
    double a[1010], b[1010];
    cin >> T;
    for (int tot = 1; tot <= T; tot++) {
        cin >> N;
        for (int i = 0; i < N; i++) 
            cin >> a[i];
        for (int i = 0; i < N; i++) {
            cin >> b[i];
        }
        sort(a, a+N);
        sort(b, b+N);
        int p1 = 0, p2 = N-1;
        
        int cnt1 = 0;
        
        for (int i = 0; i < N; i++) {
            if (a[i] < b[p1]) {
                p2--;
            }
            else {
                cnt1++;
                p1++;
            }
        }
        
        int cnt2 = N;
        for (int i = 0; i < N; i++) {
            int found = 0;
            for (int j = 0; j < N; j++) {
                if (a[i] < b[j]) {
                    b[j] = -1.0;
                    found = 1;
                    break;
                }
            }
            if (found) {
                cnt2--;
            }
                
        }
        cout << "Case #" << tot << ": " << cnt1 << " " << cnt2 << endl;
        
    }
    
    return 0;
}
