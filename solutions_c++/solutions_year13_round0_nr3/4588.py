#include<cstdio>
#include<sstream>
#include<cstdlib>
#include<cctype>
#include<cmath>
#include<algorithm>
#include<set>
#include<queue>
#include<stack>
#include<list>
#include<iostream>
#include<fstream>
#include<numeric>
#include<string>
#include<vector>
#include<cstring>
#include<map>
#include<iterator>

#define SQR(x) ((x)*(x))
#define LL long long int
#define LLU long long unsigned
#define pb push_back
#define pp pop_back
#define MP make_pair
#define sz size()
#define VI vector<int>
#define QI queue<int>
#define SI stack<int>
#define ff first
#define ss second
#define MII map<int, int>
#define SD(a) scanf("%d", &a)
#define SD2(a, b) scanf("%d %d", &a, &b)
#define NL puts("")
#define CLR(a) memset(a, 0, sizeof(a))
#define SET(a) memset(a, -1, sizeof(a))
#define rep(i, init, n) for(i=init; i<n; i++)
#define repv(i, init, n) for(i=init; i>n; i--)
#define rep1(i, init, n) for(i=init; i<=n; i++)
#define repv1(i, init, n) for(i=init; i>=n; i--)
#define READ(f) freopen(f, "r", stdin)
#define WRITE(f) freopen(f, "w", stdout)

#define MAXN 10010
#define EPS 1e-9
#define INF 2147483647
#define MOD 747474747
#define pi acos(-1.0)
using namespace std;
int store[1005];
char test[20];
bool ispalindrome(int len)
{
    int i, j;
    for(i=0, j=len-1; i<=j; i++, j--)
    {
        if(test[i]!=test[j]) break;
    }
    if(i<=j) return 0;
    return 1;
}
void call()
{
    int i, d, k, sq;
    store[0]=0;
    sq=sqrt(1000);
    for(i=1; i<=1000; i++)
    {
        int num=i;
        k=0;
        while(num)
        {
            test[k++]=num%10+'0';
            num/=10;
        }
        if(ispalindrome(k))
        {
            num=sqrt(i);
            if(num*num==i)
            {
                k=0;
                while(num)
                {
                    test[k++]=num%10+'0';
                    num/=10;
                }
                if(ispalindrome(k)) store[i]=store[i-1]+1;
                else store[i]=store[i-1];
            }
            else store[i]=store[i-1];
        }
        else store[i]=store[i-1];
        //printf("%d ", store[i]);
    }
}
int main()
{
    //READ("C-small-attempt0.in");
    //WRITE("output.txt");
    int ncase, tcase, a, b, sq, sa, sb;
    call();
    SD(ncase);
    rep1(tcase, 1, ncase)
    {
        SD2(a, b);
        printf("Case #%d: %d\n", tcase, store[b]-store[a-1]);
    }
    return 0;
}
