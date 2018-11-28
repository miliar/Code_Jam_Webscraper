#include <cstdio>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;

ifstream cin("A.in");
ofstream cout("A.out");

int t, a, n, t_case, i;
int v[5000];

int get_cost(int &a, int x) {
    
    int step = 0;

    while(a <= x) {
        a += a - 1;
        step++;
    }

    return step;
}

int main() {
    
    cin >> t;
    
    for(t_case = 1; t_case <= t; ++t_case) {
        int a, n;
        cin >> a >> n;

        for(i = 1; i <= n; ++i)
            cin >> v[i];

        sort(v + 1, v + n + 1);
        
        i = 1;

        int current_add = 0;
        int ans = 1000 * 1000 * 1000;

        while(i <= n) {
            
            for(; i <= n && a > v[i]; ++i) 
                a += v[i];
            
            ans = min(ans, current_add + n - i + 1);

            if(i <= n) {
                int to_add = v[i] + 1 - a;
                if(a == 1) {
                    //current_add += n - i + 1;
                    i = n + 1;
                }
                else {
                    current_add += get_cost(a, v[i]);
                }
            }
        }

        cout << "Case #" << t_case << ": " << ans << "\n";
    }

    return 0;
}
