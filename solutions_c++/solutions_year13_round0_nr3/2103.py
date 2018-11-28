#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <cstring>
#include <cassert>
using namespace std;

#define FOR(i,a,n) for(int i = (int)a; i < (int)n; i++)
#define REP(i,n) FOR(i,0,n)
#define FORE(it,c) for(__typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define ALL(c) c.begin(), c.end()
#define CLEAR(c,v) memset(c,v,sizeof(c))

typedef long long int lli;
typedef pair<int,int> ii;

lli A[] = {
0, 1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401ll, 121242121ll, 123454321ll, 125686521ll, 400080004ll, 404090404ll, 10000200001ll, 10221412201ll, 12102420121ll, 12345654321ll, 40000800004ll, 1000002000001ll, 1002003002001ll, 1004006004001ll, 1020304030201ll, 1022325232201ll, 1024348434201ll, 1210024200121ll, 1212225222121ll, 1214428244121ll, 1232346432321ll, 1234567654321ll, 4000008000004ll, 4004009004004ll};

int main(){
    ios::sync_with_stdio(false);
    int len = 40;
    int tcase;
    cin >> tcase;
    FOR(tc, 1, tcase + 1) {
        lli a, b;
        cin >> a >> b;
        
        int cnt = 0;
        REP(i, len) if(A[i] >= a and A[i] <= b) cnt++;

        cout << "Case #" << tc << ": " << cnt << endl;
    }
    
    return 0;
}

