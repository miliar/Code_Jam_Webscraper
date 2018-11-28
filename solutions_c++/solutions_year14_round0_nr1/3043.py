#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <complex>
#include <utility>
#include <fstream>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cctype>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>

using namespace std;

#define REP(i,a,b) for(int i=a;i<b;i++)
#define REV(i,a,b) for(int i=a-1;i>=b;i--)
#define GI ({ int x; scanf("%d",&x); x; })
#define ALL(v) v.begin(),v.end()
#define PB push_back
#define MP make_pair
#define PQ priority_queue
#define MAXX (int)(1e9)
#define MINN (double)(1e-9)
#define PI (double)(3.141592653589793238)

typedef long long LL;
typedef unsigned long long ULL;
typedef vector <int> VI;
typedef vector <string> VS;
typedef vector <vector <int> > VVI;
typedef pair <int,int> PII;

int main()
{
    int T;
    int row1,row2;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    int ar[4][4];
    vector<int> A,B;
    cin >> T;
    int ct=1;
    while(T--)
    {
        A.clear(); B.clear();
        cin >> row1;
        row1--;
        REP(i,0,4) REP(j,0,4) cin >> ar[i][j];
        REP(i,0,4) A.push_back(ar[row1][i]);
        cin >> row2;
        row2--;
        REP(i,0,4) REP(j,0,4) cin >> ar[i][j];
        REP(i,0,4) B.push_back(ar[row2][i]);
        int cnt = 0;
        int ans;
        REP(i,0,4) REP(j,0,4) { if(A[i]==B[j]) {cnt++; ans=A[i];}}
        printf("Case #%d: ",ct++);
        if(cnt == 0) cout << "Volunteer cheated!" << endl;
        else if( cnt == 1) cout << ans << endl;
        else cout << "Bad magician!" << endl;
    }
    return 0;
}
