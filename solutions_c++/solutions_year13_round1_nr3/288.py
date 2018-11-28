#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
#include <cassert>
using namespace std;

int main() {
    int T;
    int R, M, N, K;

    cin >> T;
    cin >> R >> N >> M >> K;

    assert(T == 1);
    assert(R == 100);
    assert(N == 3);
    assert(M == 5);
    assert(K == 7);

    map<vector<int>, int> all;
    map<vector<int>, map<vector<int>, int> > outcomes;

    for (int a = 2; a <= M; a++) {
        for (int b = 2; b <= M; b++) {
            for (int c = 2; c <= M; c++) {
                vector<int> v(3);
                v[0] = a;
                v[1] = b;
                v[2] = c;
                sort(v.begin(), v.end());
                all[v]++;
            }
        }
    }

    for (map<vector<int>, int>::iterator it = all.begin(); it != all.end(); it++) {
        vector<int> numbers = it->first;
        map<vector<int>, int> outcome;

        vector<int> a;
        for (int bit = 0; bit < (1<<N); bit++) {
            int mult = 1;
            for (int i = 0; i < N; i++) {
                if ((bit & (1<<i)) != 0) {
                    mult *= numbers[i];
                }
            }
            a.push_back(mult);
        }
        
        for (int za = 0; za < (1<<N); za++)
        for (int zb = 0; zb < (1<<N); zb++)
        for (int zc = 0; zc < (1<<N); zc++)
        for (int zd = 0; zd < (1<<N); zd++)
        for (int ze = 0; ze < (1<<N); ze++)
        for (int zf = 0; zf < (1<<N); zf++)
        for (int zg = 0; zg < (1<<N); zg++)
        {
            vector<int> b(7);
            b[0] = a[za];
            b[1] = a[zb];
            b[2] = a[zc];
            b[3] = a[zd];
            b[4] = a[ze];
            b[5] = a[zf];
            b[6] = a[zg];
            sort(b.begin(), b.end());
            outcome[b]++;
        }

        outcomes[numbers] = outcome;
    }

    cout << "Case #1:" << endl;
    for (int i = 0; i < R; i++) {
        vector<int> product(K);
        for (int i = 0; i < K; i++) {
            cin >> product[i];
        }
        sort(product.begin(), product.end());

        int bestFrequency = -1;
        vector<int> bestAnswer;
        for (map<vector<int>, int>::iterator it = all.begin(); it != all.end(); it++) {
            map<vector<int>, int> outcome = outcomes[it->first];
            int freq = it->second * outcome[product];
            if (freq > bestFrequency) {
                bestFrequency = freq;
                bestAnswer = it->first;
            }
        }
        for (size_t i = 0; i < bestAnswer.size(); i++) {
            cout << bestAnswer[i];
        }
        cout << endl;
    }

    return 0;
}

