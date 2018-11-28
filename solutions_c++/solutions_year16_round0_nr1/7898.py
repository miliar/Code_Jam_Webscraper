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

int N,i,j,T,cnt,seen[10];

int update()
{
    int temp = N;
    while(temp)
    {
        int dig = temp % 10;
        if(!seen[dig]) {
            seen[dig] = 1;
            cnt++;
        }
        temp /= 10;
    }
    return cnt;
}

int main()
{
    s(T);
    int t;
    repr(t, 1, T)
    {
        s(N);
        printf("Case #%d: ", t);
        if(N == 0) {
            printf("INSOMNIA\n");
            continue;
        }
        cnt = 0;
        clr(seen, 0);
        int orig = N;
        while(update() != 10)
            N += orig;
        printf("%d\n", N);
    }   
    
    return 0;
}

