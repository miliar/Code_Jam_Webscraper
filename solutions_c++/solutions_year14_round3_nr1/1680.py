#include <iostream>
#include <string>
using namespace std;

typedef long long int i64;

i64 gcd(i64 a, i64 b) {
    return b==0?a:gcd(b, a%b);
}

i64 solve(const string &pq) {
    int i=0, N=pq.size();
    i64 a=0, b=0;
    for (i=0; i<N && pq[i]!='/'; ++i) a = a*10+pq[i]-'0';
    for (++i; i<N; ++i) b = b*10+pq[i]-'0';
    i64 ans = gcd(a, b);
    a=a/ans, b=b/ans;

    int ca=0, cb=0, bb=1;
    for (; a!=0; a/=2) ++ca;
    for (int c=b; c!=0; c/=2) ++cb, bb*=2;
    return bb/2==b?cb-ca:-1;
}

int main() {
    int casenum; cin>>casenum;
    for (int casei=1; casei<=casenum; ++casei) {
        string pq; cin >> pq;
        int ans = solve(pq);
        if (ans>=0)
            cout << "Case #" << casei << ": " << ans << endl;
        else cout << "Case #" << casei << ": impossible" << endl;
    }
    return 0;
}
