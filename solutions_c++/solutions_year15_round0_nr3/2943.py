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
#define READ  freopen("C:\\Users\\emotionless\\Desktop\\uva 13-01-15\\codejam\\C-small-attempt2.in","r",stdin)
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
string str;
int dp[10009][10][4];
int n;

int mix(int a, int b)
{

    if(a == 1 && b == 1) return 5;
    if(a == 1)
        return (b + 4);
    if(b == 1)
        return (a + 4);
    if(a == 2 && b == 2) return 1;
    if(a == 3 && b == 3) return 1;
    if(a == 4 && b == 4) return 1;

    if(a == 2 && b == 3) return 8;
    if(a == 2 && b == 4) return 3;
    if(a == 3 && b == 2) return 4;
    if(a == 3 && b == 4) return 6;
    if(a == 4 && b == 3) return 2;
    if(a == 4 && b == 2) return 7;
}


int solve(int ind, int pre, int cs)
{
    if(ind == n)
    {
        if(cs == 3 && pre == 8) return 1;
        return 0;
    }

    int &ret = dp[ind][pre][cs];
    if(ret != -1) return ret;
    ret = 0;
    int g = mix(pre, str[ind] - 'i' + 2);

    ret = solve(ind + 1, pre < 5? ((g < 5?g+4:g-4)):mix(pre - 4, str[ind] - 'i' + 2), cs);
    if(pre == 6 && cs == 1)
        ret += solve(ind + 1, str[ind] - 'i' + 6, cs + 1);
    if(pre == 7 && cs == 2)
        ret += solve(ind + 1, str[ind] - 'i' + 6, cs + 1);
//    cout<<ind<<" "<<pre<<" "<<g<<" "<<cs<<" "<<ret<<endl;
    return ret;
}



int main()
{
    READ;
    WRITE;
    int i, j;
    int num;
    string tmp;
    int t,m, cases = 1;
    scanf("%d", &t);

    while(t--)
    {
        cin>>n>>m;
        cin>>tmp;
        str = "";
        for(i = 1; i <= m; i++)
            str = str + tmp;
//        cout<<str<<endl;
        n = n*m;
        memset(dp, -1, sizeof dp);
        int res = solve(1, str[0] - 'i' + 6,1);
//        cout<<res<<endl;
        if(res)
        printf("Case #%d: YES\n", cases++);
        else
        printf("Case #%d: NO\n", cases++);
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
