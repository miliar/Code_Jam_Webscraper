#include <bits/stdc++.h>
using namespace std;

#define pb push_back
#define mp make_pair
#define all(X) (X).begin(),(X).end()
#define clr(X,a) memset((X), (a), sizeof((X)))
#define s(a) scanf("%d", &a)
#define ps(a) printf("%d ", a)
#define pn(a) printf("%d\n", a)
#define rep(i,n) for(i = 0; i < (n); i++)
#define repr(i,a,b) for(i = (a); i <= (b); i++)

int N,i,j,T;
char str[110];

int main()
{
    s(T);
    int t = 1;
    repr(t, 1, T)
    {
        scanf("%s", str);
        string s = str;
        s += '+';
        N = (int)s.size();
        int ans = 0;
        for(i = N-1; i >= 1; i--)
            if(s[i] != s[i-1])
                ans++;
        printf("Case #%d: %d\n", t, ans);
    }   
    
    return 0;
}

