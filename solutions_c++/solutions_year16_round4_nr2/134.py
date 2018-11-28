#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdlib>
#include <vector>

using namespace std;

int n, k;
vector<double> arr1, arr2;

void merge(double *a, double *b, double *c, int n) {
    for (int i = 0; i <= n ; i++) c[i] = 0.0;
    for (int pa = 0; pa <= n; pa++) {
        for (int pb = 0; pa + pb <= n; pb++) {
            c[pa + pb] += a[pa] * b[pb];
        }
    }
}

double t1[210][210];
double t2[210][210];
double t3[210][210];
double t4[210][210];

void build(double *tar, double *src, double val) {
    for (int i = 0; i <= n; i++) {
        tar[i] = src[i] * (1.0 - val);
    }
    for (int i = 1; i <= n; i++) {
        tar[i] += src[i - 1] * val;
    }
}

void build() {
    for (int i = 1; i <= n; i++) {
        t1[0][i] = 0.0;
        t2[0][i] = 0.0;
        t3[0][i] = 0.0;
        t4[0][i] = 0.0;
    }
    t1[0][0] = 1.0;
    t2[0][0] = 1.0;
    t3[0][0] = 1.0;
    t4[0][0] = 1.0;
    for (int i = 1; i <= arr1.size(); i++) {
        build(t1[i], t1[i - 1], arr1[i - 1]);
        build(t2[i], t2[i - 1], arr1[arr1.size() - i]);
    }
    for (int i = 1; i <= arr2.size(); i++) {
        build(t3[i], t3[i - 1], arr2[i - 1]);
        build(t4[i], t4[i - 1], arr2[arr2.size() - i]);
    }
}

int main() {
    int tc;
    cin >> tc;
    for (int t = 1; t <= tc; t++) {
        arr1.clear();
        arr2.clear();
        cin >> n >> k;
        for (int i = 0; i < n; i++) {
            double tmp;
            cin >> tmp;
            if (tmp >= 0.5) arr1.push_back(tmp);
            else arr2.push_back(tmp);
        }
        sort(arr1.begin(), arr1.end());
        sort(arr2.begin(), arr2.end());
        
        build();
        
        double ans = 0.0;
        
        for (int s1 = 0; s1 <= arr1.size(); s1++) {
            for (int s2 = 0; s1 + s2 <= arr1.size(); s2++) {
                if (k - s1 - s2 > arr2.size()) continue;
                for (int s3 = 0; s3 <= arr2.size(); s3++) {
                    int s4 = k - s1 - s2 - s3;
                    if (s4 < 0 || s3 + s4 > arr2.size()) continue;
                    double tar[210], tar1[210], tar2[210];
                    merge(t1[s1], t2[s2], tar1, k / 2);
                    merge(t3[s3], t4[s4], tar2, k / 2);
                    merge(tar1, tar2, tar, k / 2);
                    ans = max(ans, tar[k / 2]);
                }
            }
        }
        
        printf("Case #%d: %.15f\n", t, ans);
    }
    
    return 0;
}

