#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <cmath>
using namespace std;
typedef long long LL;
#define N 105
int ca;
int n , a[N];
string s[N] , S;
int L , ans;
bool f[N];


void work()
{
    printf("Case #%d: " , ++ca);

    int i , j , k ;
    L = 0;
    scanf("%d",&n);
    for (i = 0 ; i < n ; ++ i) {
        cin >> S;
        s[i] = "";
        s[i] += S[0];
        for (j = 1 ; j < S.size() ; ++ j)
            if (S[j] != S[j - 1])
                s[i] += S[j];
        L += s[i].size();
        a[i] = i;
    }
    ans = 0;
    do {
        S = "";
        for (i = 0 ; i < n ; ++ i)
            S += s[a[i]];
        memset(f , 0 , sizeof(f));
        for (j = 0 ; j < L ; ++ j) {
            if (f[S[j] - 'a']) {
                break;
            }
            f[S[j] - 'a'] = 1;
            while (S[j + 1] == S[j])
                ++ j;
        }
        if (j >= L)
            ++ ans ;//, cout << S << endl;
    }while(next_permutation(a , a + n));


    cout << ans << endl;
}

int main()
{
    freopen("1.txt" , "r" , stdin);
    freopen("2.txt" , "w" , stdout);

    int _; scanf("%d", &_); while (_ --)
        work();
    return 0;
}
