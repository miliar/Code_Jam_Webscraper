#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

long long getmin(long long n, long long p) {
    if (p == n) return n - 1;
    long long x = 0, lst = 1;
    while(true) {
        p -= n / 2;
        if (p <= 0) {
            break;
        }
        n /= 2;
        x += lst;
        lst *= 2;
    }
    return x * 2;
}

long long maxplace(long long n, long long m) {
    long long place = n - 1;
    while(true) {
        if (m != n - 1) {
            m -= m / 2;
            n /= 2;
            place /= 2;
        } else {
            break;
        }
    }
    return place;
}

long long getmax(long long n, long long p) {
    long long L = -1, R = n;
    while(R - L > 1) {
        long long M = (L + R) / 2;
        if (maxplace(n, M) > p - 1) {
            R = M;
        } else {
            L = M;
        }
    }
    return L;
}



void test(long long n) {

    for(int i = 0; i < n; ++i) {
        cout << maxplace(n, i) << endl;
    }
    return;


    vector<pair<vector<int>, int> > v;
    v.resize(n);
    for(int i = 0; i < v.size(); ++i) {
        v[i] = make_pair(vector<int>(), i);
    }
    while(n) {
        for(int i = 0; i < v.size(); ++i) {
            cout << v[i].second << " ";
        }
        cout << endl;
        for(int i = 0; i < v.size(); i += 2) {
            v[i].first.push_back(0);
            v[i + 1].first.push_back(1);
        }
        sort(v.begin(), v.end());
        n /= 2;
    }
        for(int i = 0; i < v.size(); ++i) {
            cout << v[i].second << " ";
        }
        cout << endl;
        cout << endl;

    vector<int> s;
    for(int i = 0; i < v.size(); ++i) {
        s.push_back(v[i].second);
        for(int j = 0;;++j) {
            bool fnd = false;
            for(int w = 0; w <= s.size(); ++w) {
                if (s[w] == j) {
                    fnd = true;
                    break;
                }
            }
            if (!fnd) {
                cout << i + 1 << ": " << j - 1 << "   " << getmin(v.size(), i + 1) << endl;
                break;
            }
        }
    }
}

int main() {
    //test(8);
    //return 0;
    int T;
    cin >> T;
    for(int t = 0; t < T; ++t) {
        cerr << t << endl;
        long long n, p;
        cin >> n >> p;
        long long r = 1;
        while(n) {
            r *= 2;
            --n;
        }
        n = r;
        cout << "Case #" << t + 1 << ": ";
        cout << getmin(n, p) << " ";
        cout << getmax(n, p);
        cout << endl;
    }
}
