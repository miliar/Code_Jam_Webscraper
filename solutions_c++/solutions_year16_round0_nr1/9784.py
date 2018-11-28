#include <bits/stdc++.h>
using namespace std;

#define REP(i,a,b) for (int i = (a); i<= (b); ++i)
#define REPD(i,a,b) for (int i = (a); i>= (b); --i)
#define FORI(i,n) REP(i,1,n)
#define FOR(i,n) REP(i,0,int(n)-1)
#define mp make_pair
#define pb push_back
#define pii pair<int,int>
#define vi vector<int>
#define ll long long
#define SZ(x) int((x).size())
#define DBG(v) cerr << #v << " = " << (v) << endl;
#define FOREACH(i,t) for (auto i = t.begin(); i != t.end(); ++i)
#define fi first
#define se second

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T,N;
    cin >> T;
    unordered_map<int,int> tab;
    FOR(i,1e6+1) {
        int c = 0;
        int num = i;
        if(num==0)
            c = 1;
        while(num>0) {
            c |= (1<<(num%10));
            num /= 10;
        }
        tab[i]=c;
    }
    FOR(t,T) {
        cin >> N;
        if(N==0) {
            cout << "Case #" << t+1 << ": " << "INSOMNIA" << endl;
            continue;
        }
        int r = 0;
        int temp = 0;
        while(r != 1023) {
            temp += N;
            r |= tab[temp];
        }
        cout << "Case #" << t+1 << ": " << temp << endl;
    }
    return 0;
}
