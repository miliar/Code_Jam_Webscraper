
#include <bits/stdc++.h>
using namespace std;

#define si(n) scanf("%d", &n)
#define sl(n) scanf("%I64d", &n)
#define sd(n) scanf("%lf", &n)
#define pi(n) printf("%d", n)
#define pl(n) printf("%I64d", n)
#define pd(n) printf("%lf", n)
#define spc printf(" ")
#define ntr printf("\n")
#define c(n) cin>>n
#define o(n) cout<<n
#define lin(n) getline(cin, n)
#define lp(i, m, n) for(i = m; i < n; i++)
#define lll long long
#define ul unsigned long long
#define pf printf
#define gtl(n) getline(cin,n)
#define sf scanf
#define hello int main()
#define bye return 0
#define ef else if
#define el else
#define mii map<int, int>
#define msi map<string, int>
#define mss map<string, string>
#define mll map<long long, long long>
#define mis map<int, string>
#define xx memset
#define mmii(n) map<int,int>::iterator n

hello
{
    freopen("in.in","r",stdin);
    freopen("out.o","w",stdout);

    int i, j, k, l, m, n, t, top, tel;
    deque <char> dq;
    char a[2005];
    deque <char> :: iterator it;
    si(t); getchar();
    lp(i, 1, t+1)
    {
        gets(a);
        dq.clear();
        pf("Case #%d: ", i);
        l = strlen(a);
        top = (int)a[0];
        //tel = (int)a[0];
        dq.push_back(a[0]);
        lp(j, 1, l)
        {
            if(a[j] >= top) {dq.push_front(a[j]); top = (int)a[j];}
            el {dq.push_back(a[j]);}
        }
        for(it = dq.begin(); it != dq.end(); it++) o(*it);
        ntr;
    }
    bye;
}

