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

int T, N, P;

#ifdef __APPLE__
    ifstream fin("/Users/byunghoon/Desktop/Programs/Programs/in.txt");
    ofstream fout("/Users/byunghoon/Desktop/Programs/Programs/out.txt");
#endif

int main() {
    fin >> T;
    for (int i = 0; i < T; i++) {
        fout << "Case #" << i+1 << ": ";
        int rem = 0;
        fin >> N;
        priority_queue<pair<int, char> > pq;
        for (int j = 0; j < N; j++) {
            fin >> P;
            pq.push(make_pair(P, 'A' + j));
            rem += P;
        }
        while (!pq.empty()) {
            pair<int, char> highest = pq.top();
            pq.pop();
            fout << highest.second;
            highest.first--;
            rem--;
            if (highest.first > 0) pq.push(highest);
            if (rem != 2) {
                highest = pq.top();
                pq.pop();
                fout << highest.second;
                highest.first--;
                rem--;
                if (highest.first > 0) pq.push(highest);
            }
            fout << " ";
        }
        fout << endl;
    }
    
    return 0;
}