#include<bits/stdc++.h>
#define DIST(x1,x2, y1, y2) (((x1-x2)*(x1-x2))+((y1-y2)*(y1-y2)))
#define CLR(a) a.clear()
#define VCLR(a, n) for(int i=0; i<=n+3; i++) a[i].clear()
#define SIZE(a) a.size()
#define ERASE(a, b) memset(a, b, sizeof a)
#define PB(a, b) a.push_back(b)
#define PB2(a,i,b) a[i].push_back(b)
#define LL long long
#define DBG cout<<"I Am Here"<<endl
#define DBGA(a) cout<<a<<endl
#define DBGI(b,a) cout<<b<<' '<<a<<endl
#define DBGL(i,s,e,b) or(int i=s; i<=e; i++) cout<<b<<endl
#define INF 1e9
#define II(a) scanf("%I64d", &a)
#define PP(a) printf("%I64d", a)
#define si(a) scanf("%d", &a)
#define pii pair<LL,LL>
#define MAX 33333337
#define logbase(a, b) ( log10(a)/log10(b) )

using namespace std;

LL tobinary(LL x)
{
    LL rem, i=1, binary=0;
    while (x!=0)
    {
        rem=x%2;
        x/=2;
        binary+=rem*i;
        i*=10;
    }
    return binary;
}

LL power(LL n, LL ghat)
{
    if(ghat==0) return 1;
    else return n*power(n,ghat-1);
}

LL ton(LL bi, LL n)
{
    LL res = 0; LL ghat = 0;
    while(bi!=0)
    {
        LL rem = bi%10;
        res = res + rem*power(n,ghat);
        ghat++;
        bi = bi / 10;
    }
    return res;
}

LL isnotprime(LL x)
{
    int sz = sqrt(x);
    for(int i=2; i<=sz; i++)
    {
        if(x%i==0) return x/i;
    }
    return -1;
}

bool solve(LL x)
{
    LL arr[12];
    LL ret = tobinary(x);
    arr[2] = ton(ret, 2);
    arr[3] = ton(ret, 3); arr[4] = ton(ret, 4); arr[5] = ton(ret, 5);
    arr[6] = ton(ret, 6); arr[7] = ton(ret, 7); arr[8] = ton(ret, 8);
    arr[9] = ton(ret, 9); arr[10] = ret;
    bool flag =false;
    for(int i=2; i<=10; i++)
    {
        //cout<<arr[i]<<' ';
        arr[i] = isnotprime(arr[i]);
        if(arr[i]==-1){
            flag = true;
            return false;
        }
    }
    //cout<<endl;
    if(!flag)
    {
        printf("%lld", ret);
        for(int i=2; i<=10; i++)
        {
            printf(" %lld", arr[i]);
        }
        printf("\n");
    }
    return true;
}

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("ResC.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for(int caseno=1; caseno<=test; caseno++)
    {
        int a, b;
        scanf("%d %d", &a, &b);
        printf("Case #%d:\n", caseno);
        LL num;
        if(a==16)
        {
            int cnt = 0;
            for(LL i=32769; i<=65535; i++)
            {
                if(i%2!=0)
                {
                    if(solve(i)==true) cnt++;
                    if(cnt==b) break;
                }
            }
        }
    }
}
