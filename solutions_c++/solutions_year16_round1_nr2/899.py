#include <bits/stdc++.h>

using namespace std;

typedef pair<int, int> ii;
typedef pair<ii, int> iii;
typedef pair<ii, ii> iiii;
typedef pair<int, bool> ib;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef vector<vb> vvb;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
typedef long long ll;
typedef pair<ll, ll> pll;
typedef vector<ll> vll;
typedef vector<pll> vpll;

#ifdef __APPLE__
    ifstream fin("/Users/byunghoon/Desktop/Programs/Programs/in.txt");
    ofstream fout("/Users/byunghoon/Desktop/Programs/Programs/out.txt");
#endif

int T, N, H;

int main() {
    fin >> T;
    for (int i = 1; i <= T; i++) {
        fout << "Case #" << i << ":";
        fin >> N;
        vi h(2005, 0);
        for (int j = 0; j < 2*N-1; j++) {
            for (int k = 0; k < N; k++) {
                fin >> H;
                h[H]++;
            }
        }
        vi nums;
        for (int j = 0; j < 2505; j++)
            if (h[j] % 2 == 1) nums.push_back(j);
        sort(nums.begin(), nums.end());
        for (int a : nums)
            fout << " " << a;
        fout << endl;
    }
    
    return 0;
}