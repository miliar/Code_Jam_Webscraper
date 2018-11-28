#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#define puba push_back
#define mapa make_pair
#define ff first
#define ss second

using namespace std;

int t, n, num;

int main() {
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cin >> n;
        vector <int> mas;
        vector <int> now_pos;
        map <int, int> st_pos;
        for (int j = 0; j < n; ++j) {
            cin >> num;
            mas.puba(num);
            now_pos.puba(num);
            st_pos[num] = j;
        }
        sort(mas.begin(), mas.end());
        int l = 0, r = n - 1;
        int ans = 0;
        
        for (int j = 0; j < n; ++j) {
            if (st_pos[mas[j]] - l > r - st_pos[mas[j]]) {
                for (int k = st_pos[mas[j]]; k < r; ++k) {                    
                    st_pos[now_pos[k]] = k + 1;                    
                    st_pos[now_pos[k + 1]] = k;
                    int temp = now_pos[k];
                    now_pos[k] = now_pos[k + 1];
                    now_pos[k + 1] = temp;
                    ++ans;
                }
                --r;
            } else {
                for (int k = st_pos[mas[j]]; k > l; --k) {                    
                    st_pos[now_pos[k]] = k - 1;                    
                    st_pos[now_pos[k - 1]] = k;
                    int temp = now_pos[k];
                    now_pos[k] = now_pos[k - 1];
                    now_pos[k - 1] = temp;
                    ++ans;
                }
                ++l;
            }
        }
        cout << "Case #" << i + 1 << ": " << ans << endl;
        /*
        for (int j = 0; j < n; ++j) {
            cout << now_pos[j] << " ";
        }
        cout << endl;*/
    }

    return 0;
}