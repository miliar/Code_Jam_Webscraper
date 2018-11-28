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

int T, N, f[1005];

int main() {
    fin >> T;
    for (int i = 1; i <= T; i++) {
        fout << "Case #" << i << ": ";
        fin >> N;
        for (int j = 1; j <= N; j++)
            fin >> f[j];
        
        bool doBreak2 = false;
        for (int j = N; j >= 3; j--) {
            vi circle(N);
            for (int k = 1; k <= N; k++)
                circle[k-1] = k;
            
            do {
                /*
                for (int k = 0; k < j; k++)
                    cout << circle[k] << " ";
                cout << endl << endl;
                */
                
                if (f[circle[0]] != circle[1] && f[circle[0]] != circle[j-1]) continue;
                if (f[circle[j-1]] != circle[0] && f[circle[j-1]] != circle[j-2]) continue;
                bool doBreak = false;
                for (int k = 1; k < j-1; k++) {
                    if (f[circle[k]] != circle[k-1] && f[circle[k]] != circle[k+1]) {
                        doBreak = true;
                        break;
                    }
                }
                if (!doBreak) {
                    fout << j << endl;
                    doBreak2 = true;
                    break;
                }
            } while (next_permutation(circle.begin(), circle.end()));
            if (doBreak2) break;
        }
    }
    
    return 0;
}