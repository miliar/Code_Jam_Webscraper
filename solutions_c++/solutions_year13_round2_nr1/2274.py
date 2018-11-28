#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

pair<int,int> d;

void dist(int A, int b) {
    d.first = 0;
    if (A > b) {
        d.second = A;
    } else {
        while(A <= b) {
            d.first++;
            A += (A-1);
        }
        d.second = A;
    }

}

int main() {
    vector<int> v;
    vector<int> v2;
    int T;
    cin >> T;
    for(int i = 1; i <= T; i++) {
        v.clear();
        v2.clear();
        // read
        int A, N, tmp;
        cin >> A >> N;
        for(int u = 1; u <= N; u++) {
            cin >> tmp;
            v.push_back(tmp);
            v2.push_back(0);
        }
        std::sort(v.begin(), v.end());
        // compute
        int rez = 0;
        if (A == 1) {
            rez = v.size();
        } else {
            for(int u = 1; u <= N; u++) {
                dist(A, v[u-1]);
                A = d.second + v[u-1];
                v2[u-1] = d.first;
                //cout << " " << v2[u-1]<< ","<<A<<","<<v[u-1];
            }
            for(int u = N; u >= 1; u--) {
                if (v2[u-1] > N-u+1)
                    rez = N-u+1;
                else
                    rez = rez + v2[u-1];
            }
        }
        // write
        cout << "Case #" << i << ": " << rez << endl;
    }
}
