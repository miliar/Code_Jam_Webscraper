#include <functional>
#include <algorithm>
#include <stdexcept>
#include <iomanip>
#include <cmath>
#include <string>
#include <cstdio>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <iostream>
#include <sstream>
#include <cctype>
#include <ctime>
#include <float.h>
#include <bitset>
#include <set>
#include <utility>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <vector>

using namespace std;

#define swap(a,b) {a^=b;b^a=;a^=b;}
#define For(i,a,b) for (int i(a),_b(b); i <= _b ; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b ; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n ; ++i)
#define Repd(i,n) for (int i((n)-1); i>=0 ; --i)
inline int min(int a,int b){return a<b?a:b;}
inline int max(int a,int b){return a>b?a:b;}

long long ans[] = {1L,4L,9L,121L,484L,10201L,12321L,14641L,40804L,44944L,1002001L,1234321L,4008004L,100020001L,102030201L,104060401L,121242121L,123454321L,125686521L,400080004L,404090404L,10000200001L,10221412201L,12102420121L,12345654321L,40000800004L,1000002000001L,1002003002001L,1004006004001L,1020304030201L,1022325232201L,1024348434201L,1210024200121L,1212225222121L,1232346432321L,1234567654321L,4000008000004L,4004009004004L};

int T, rst;
long long A, B;

int main(){
    freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
    cin >> T;
    Rep(i, T){
        printf("Case #%d: ", i+1);
        cin >> A >> B;
        rst = 0;
        Rep(j, 38) if (ans[j] >= A && ans[j] <= B) rst ++;
        cout << rst << endl;   
    }
    return 0;
}