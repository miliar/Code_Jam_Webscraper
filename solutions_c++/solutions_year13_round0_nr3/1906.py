#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<vector>
#include<cstring>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<string>
#include<iterator>
#include<string>
#include<sstream>
#include<cassert>
#include<ctime>
#include<cmath>

#define MP make_pair
#define PB push_back
#define X first
#define Y second
#define oo 2000000000
#define MOD 1000000007
#define LL long long int
#define PII pair<int,int>
#define DEBUG 0

using namespace std;
LL ar[] =
{1LL,
4LL,
9LL,
121LL,
484LL,
10201LL,
12321LL,
14641LL,
40804LL,
44944LL,
1002001LL,
1234321LL,
4008004LL,
100020001LL,
102030201LL,
104060401LL,
121242121LL,
123454321LL,
125686521LL,
400080004LL,
404090404LL,
10000200001LL,
10221412201LL,
12102420121LL,
12345654321LL,
40000800004LL,
1000002000001LL,
1002003002001LL,
1004006004001LL,
1020304030201LL,
1022325232201LL,
1024348434201LL,
1210024200121LL,
1212225222121LL,
1214428244121LL,
1232346432321LL,
1234567654321LL,
4000008000004LL,
4004009004004LL,
100000020000001LL,
100220141022001LL,
102012040210201LL,
102234363432201LL,
121000242000121LL,
121242363242121LL,
123212464212321LL,
123456787654321LL};
int L;
int get(LL x){
    return upper_bound(ar,ar+L,x) - ar;
}
int main(){
    L = sizeof(ar)/sizeof(ar[0]);
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    LL a,b;
    scanf("%d",&T);
    for(int I=1;I<=T;I++){
        scanf("%lld%lld",&a,&b);
        printf("Case #%d: %d\n",I,get(b)-get(a-1));
    }
    return 0;
}
