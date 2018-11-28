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
#define READ  freopen("C:\\Users\\emotionless\\Desktop\\uva 13-01-15\\codejam\\D-small-attempt3.in","r",stdin)
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

///***** Template ends here *****///
///********************* Code starts here ****************************

#define YES printf("GABRIEL\n")
#define NO printf("RICHARD\n")



int main()
{
    READ;
    WRITE;
    int i, j;
    int num;
    string tmp;
    int t,m,n,cases = 1;
    scanf("%d", &t);
    int x;
    while(t--)
    {
        scanf("%d %d %d", &x, &n, &m);
        printf("Case #%d: ", cases++);
        if(x == 1) YES;
        else if((n*m)%x > 0) NO;
        else if(x == 2)
        {
            if((n * m)%2==0) YES;
            else NO;
        }
        else if(x == 3)
        {
            if(n == 2 && m == 3) YES;
            else if(n == 3 && m == 2) YES;
            else if(n == 3 && m == 4) YES;
            else if(n == 4 && m == 3) YES;
            else if(n == 3 && m == 3) YES;
            else NO;
        }
        else
        {
            if(n == 4 && m == 3) YES;
            else if(n == 3 && m == 4) YES;
            else if(n == 4 && m == 4)YES;
            else NO;
        }
    }



    return 0;
}

/*



1
2 6
ji


1
9 1
kikijijkj

*/
