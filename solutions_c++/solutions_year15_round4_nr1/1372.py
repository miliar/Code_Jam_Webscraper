#include<bits/stdc++.h>

#define xx first
#define yy second
#define all(a) a.begin(), a.end()
#define vsort(v) sort(all(v))
#define UNIQUE(a)  sort(all(a)); a.erase(unique(all(a)), a.end())
#define clr(a,k) memset(a,k,sizeof a)
#define bclr(b) memset(b,false,sizeof b)
#define fr(i, a) for(i = 0; i < a; i++)
#define frr(i,a) for(i = a - 1; i >= 0, i--)
#define LL long long
#define pb push_back
#define pii pair<int, int>
#define mp make_pair
#define vi vector<int>
#define vll vector<long long>
///***** bit *****///
#define check_bit(a, b) (a&(1<<b))
#define set_bit(a, b) (a|(1<<b))
#define total_bit(a) __builtin_popcount(a)
///***** Input / Output *****///
// IO
#define READ  freopen("C:\\Users\\emotionless\\Desktop\\uva 13-01-15\\codejam\\input.in","r",stdin)
#define WRITE freopen("C:\\Users\\emotionless\\Desktop\\uva 13-01-15\\codejam\\output.txt","w",stdout)
#define use_cin  ios_base::sync_with_stdio(0); cin.tie(0);


#define s1(a) scanf("%d", &a)
#define s2(a, b) scanf("%d %d", &a, &b)
#define s3(a, b, c) scanf("%d %d %d", &a, &b, &c)
#define p1(a) printf("%d", a)
#define p2(a, b) printf("%d %d", a, b)
#define p3(a, b, c) printf("%d %d %d", a, b, c)


#define MOD 1000000007
#define MAX 200009



using namespace std;
///******* Template ********///


template <class T> inline T bigmod(T p,T e,T M)
{
    if(e==0)return 1;
    if(e%2==0)
    {
        T t=bigmod(p,e/2,M);
        return (t*t)%M;
    }
    return (bigmod(p,e-1,M)*p)%M;
}
template <class T> inline T gcd(T a,T b)
{
    if(b==0)return a;
    return gcd(b,a%b);
}
template <class T> inline T modinverse(T a,T M)
{
    return bigmod(a,M-2,M);
}


//int dr[] = {-1, 0, 1, 0}; int dc[] = {0, 1, 0, -1}; /// 4 sides
//int dr[] = {-1, -1, 0, 1, 1, 1, 0, -1}; dc[] = {0, 1, 1, 1, 0, -1, -1, -1}; /// 8 sides


///***** Template ends here *****///
///********************* Code starts here ****************************

#define YES printf("GABRIEL\n")
#define NO printf("RICHARD\n")


string str[109];


int main()
{
    READ;
    WRITE;
    int i, j, k;
    int num;
    int t,m,cases = 1;
    int x, n;
    cin>>t;
    while(t--)
    {
        cin>>n>>m;
        for(i = 0; i < n; i++)
            cin>>str[i];
        int cnt = 0;
        bool ok = 0;

        for(i = 0; i < n; i++)
        {
            for(j = 0; j < m; j++)
            {
                int tot = 0;
                if(str[i][j] != '.')
                {
                    for(k = j + 1; k < m; k++)
                        if(str[i][k] != '.') break;
                    if(k == m)
                        tot++;
                    for(k = j - 1; k >= 0; k--)
                        if(str[i][k] != '.') break;
                    if(k == -1)
                        tot++;

                    for(k = i + 1; k < n; k++)
                        if(str[k][j] != '.') break;
                    if(k == n)
                        tot++;
                    for(k = i - 1; k >= 0; k--)
                        if(str[k][j] != '.') break;
                    if(k == -1)
                        tot++;
                }
                if(tot == 4)
                {
                    ok = 1;
                }
            }
        }
        printf("Case #%d: ", cases++);
        if(ok)
        {
            cout<<"IMPOSSIBLE"<<endl;
            continue;
        }



        for(i = 0; i < n; i++)
        {
            for(j = 0; j < m; j++)
            {
                if(str[i][j] != '.')
                {
                    if(str[i][j] == '>')
                    {
                        for(k = j + 1; k < m; k++)
                            if(str[i][k] != '.') break;
                        if(k == m)
                            cnt++;
                    }
                    if(str[i][j] == 'v')
                    {
                        for(k = i + 1; k < n; k++)
                            if(str[k][j] != '.') break;
                        if(k == n)
                            cnt++;
                    }
                    if(str[i][j] == '<')
                    {
                        for(k = j - 1; k >= 0; k--)
                            if(str[i][k] != '.') break;
                        if(k == -1)
                            cnt++;
                    }
                    if(str[i][j] == '^')
                    {
                        for(k = i - 1; k >= 0; k--)
                            if(str[k][j] != '.') break;
                        if(k == -1)
                            cnt++;
                    }
                }
            }
        }
        cout<<cnt<<endl;
    }









    return 0;
}

/*


1 5 30
1 5 9 10 14


3 3
^>>
.^.
<.v



*/
