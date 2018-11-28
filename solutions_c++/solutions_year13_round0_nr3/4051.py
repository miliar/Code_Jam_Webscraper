/* Michał Adamczyk, majkello */
#include<cstdio>
#define REP(i,n) for(int i=0;i<(n);++i)
typedef long long LL;

/* haskell - preprocessing
 *
 * pal 0 _ = [""]
 * pal 1 0 = [[x] | x <- ['1'..'9']]
 * pal 1 1 = [[x] | x <- ['0'..'9']]
 * pal n 0 = [x++y++x | x <- pal 1 0, y <- pal (n-2) 1]
 * pal n 1 = (pal n 0) ++ ["0"++y++"0" | y <- pal (n-2) 1]
 *
 * palindromes = 0:[read x :: Int | n <- [1..7], x <- pal n 0]
 *
 * is_pal n = x == reverse x where x = show n
 *
 * fpal = [ x*x | x <- palindromes, is_pal $ x*x ]
 */

LL fpal[40] = {0LL,1LL,4LL,9LL,121LL,484LL,10201LL,12321LL,14641LL,40804LL,
    44944LL,1234321LL,1002001LL,4008004LL,121242121LL,123454321LL,125686521LL,
    100020001LL,102030201LL,104060401LL,400080004LL,404090404LL,12345654321LL,
    12102420121LL,10221412201LL,10000200001LL,40000800004LL,1232346432321LL,
    1234567654321LL,1210024200121LL,1212225222121LL,1214428244121LL,
    1020304030201LL,1022325232201LL,1024348434201LL,1000002000001LL,
    1002003002001LL,1004006004001LL,4000008000004LL,4004009004004LL};

void solve(int testCase) {
    int res = 0;
    LL a ,b;
    scanf("%lld%lld",&a,&b);
    REP(i,40) if(fpal[i] >= a && fpal[i] <= b) ++res;

    printf("Case #%d: %d\n", testCase, res);
}

int main() {
    int _T;
    scanf("%d",&_T);
    REP(i,_T) solve(i+1);
    return 0;
}

