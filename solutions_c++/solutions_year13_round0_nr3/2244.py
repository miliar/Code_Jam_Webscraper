#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <climits>
#include <cctype>
#include <cmath>
#include <sstream>
#include <cstdlib>
#include <climits>
#include <ctime>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <deque>
#include <queue>
#include <stack>
#include <iomanip>
#include <complex>
#include <list>
#include <bitset>
#include <fstream>
#include <limits>
#include <memory.h>

using namespace std;

#define REP(i,n) for( (i)=0 ; (i)<(n) ; (i)++ )
#define rep(i,x,n) for( (i)=(x) ; (i)<(n) ; (i)++ )
#define REV(i,n) for( (i)=(n) ; (i)>=0 ; (i)-- )
#define FORIT(it,x) for( (it)=(x).begin() ; (it)!=(x).end() ; (it)++ )
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define rforeach(it,c) for(__typeof((c).rbegin()) it=(c).rbegin();it!=(c).rend();++it)
#define foreach2d(i, j, v) foreach(i,v) foreach(j,*i)
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define SZ(x) (x).size()
#define MMS(x,n) memset(x,n,sizeof(x))
#define pb push_back
#define mp make_pair
#define UN(x) sort(all(x)),x.erase(unique(all(x)),x.end())
#define CV(x,n) count(all(x),(n))
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

typedef unsigned long long ull;

string arr[39];

void fun()
{
    arr[0] = "1";
    arr[1] = "4";
    arr[2] = "9";
    arr[3] = "121";
    arr[4] = "484";
    arr[5] = "10201";
    arr[6] = "12321";
    arr[7] = "14641";
    arr[8] = "40804";
    arr[9] = "44944";
    arr[10] = "1002001";
    arr[11] = "1234321";
    arr[12] = "4008004";
    arr[13] = "100020001";
    arr[14] = "102030201";
    arr[15] = "104060401";
    arr[16] = "121242121";
    arr[17] = "123454321";
    arr[18] = "125686521";
    arr[19] = "400080004";
    arr[20] = "404090404";
    arr[21] = "10000200001";
    arr[22] = "10221412201";
    arr[23] = "12102420121";
    arr[24] = "12345654321";
    arr[25] = "40000800004";
    arr[26] = "1000002000001";
    arr[27] = "1002003002001";
    arr[28] = "1004006004001";
    arr[29] = "1020304030201";
    arr[30] = "1022325232201";
    arr[31] = "1024348434201";
    arr[32] = "1210024200121";
    arr[33] = "1212225222121";
    arr[34] = "1214428244121";
    arr[35] = "1232346432321";
    arr[36] = "1234567654321";
    arr[37] = "4000008000004";
    arr[38] = "4004009004004";
}

bool cmp(string s1, string s2)
{
    if(SZ(s1)!=SZ(s2))
        return SZ(s1)<SZ(s2);
    return s1<=s2;
}

int main()
{
    READ("C-large-1.in");
    WRITE("C-large-1.out");
    int i, t, k, cnt;
    string A, B;
    fun();
    scanf("%d",&t);
    rep(k,1,t+1)
    {
        cnt=0;
        cin >> A >> B;
        REP(i,39) if(cmp(A,arr[i]) && cmp(arr[i],B)) cnt++;
        printf("Case #%d: %d\n",k,cnt);
    }
    return 0;
}
