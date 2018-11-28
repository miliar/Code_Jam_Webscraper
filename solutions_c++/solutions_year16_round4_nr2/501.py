#include <iostream>
#include <cstdio>
#include <bitset>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
using namespace std;
typedef long long ll;

double ptie(vector<double> p) {
    vector<double> probs;
    probs.push_back(1.0);
    for (double d : p) {
        vector<double> newp;
        newp.push_back(0.0);
        for (int i=0; i<(int)probs.size(); i++) {
            newp.back() += probs[i] * (1-d);
            newp.push_back(probs[i] * d);
        }
        probs = newp;
    }
    return probs[p.size()/2];
}

int main()
{
    int nt;
    cin >> nt;
    for (int t=1; t<=nt; t++) {
        int n,k;
        cin >> n >> k;
        double p[n];
        for (int i=0; i<n; i++)
            cin >> p[i];
        sort(p,p+n);
        double maxp=0.0;
        for (int i=0; i<=k; i++) {
            vector<double> chosen;
            for (int j=0; j<i; j++) chosen.push_back(p[j]);
            for (int j=n-k+i; j<n; j++) chosen.push_back(p[j]);
            maxp = max(maxp, ptie(chosen));
        }
        printf("Case #%d: %.7f\n", t, maxp);
    }
}
