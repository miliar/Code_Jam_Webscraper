#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define RFOR(i,a,b) for(int i=(a);i>=(b);--i)
typedef long long LL;

int plist[10000],pcount=0;

int prime(int n){
	int i;
	if ((n!=2&&!(n%2))||(n!=3&&!(n%3))||(n!=5&&!(n%5))||(n!=7&&!(n%7)))
		return 0;
	for (i=0;plist[i]*plist[i]<=n;i++)
		if (!(n%plist[i]))
			return 0;
	return n>1;
}

void initprime(){
	int i;
	for (plist[pcount++]=2,i=3;i<50;i++)
		if (prime(i))
			plist[pcount++]=i;
}

void run() {
    int N, J;
    cin >> N >> J;
    vector<LL> toAdd(11, 1);
    FOR(i,2,10) {
        REP(j,N-1) toAdd[i] = toAdd[i] * i;
        ++toAdd[i];
    }
    int all = (1 << (N - 2));
    REP(st,all) {
        vector<int> mm;
        bool isok = true;
        FOR(b,2,10) {
            LL val = 0;
            REP(i,N-2) {
                val = val * b;
                if (st & (1 << i)) ++val;
            }
            val = val * b + toAdd[b];
            bool isp = true;
            REP(i,pcount) {
                if (val % plist[i] == 0) {
                    isp = false;
                    mm.push_back(plist[i]);
                    break;
                }
            }
            if (isp) {
                isok = false;
                break;
            }
        }
        if (isok) {
            cout << "1";
            REP(i,N-2) {
                if (st & (1 << i)) cout << "1";
                else cout << "0";
            }
            cout << "1";
            REP(i,mm.size()) cout << " " << mm[i];
            cout << endl;
            if (--J == 0) break;
        }
    }
}

int main() {
    initprime();
    int k;
    cin >> k;
    FOR(c,1,k) {
        cout << "Case #" << c << ":" << endl;
        run();
    }
    return 0;
}
