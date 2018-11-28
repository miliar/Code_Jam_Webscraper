/*
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <iomanip>

using namespace std;
#pragma comment(linker, "/STACK:102400000,102400000")
#define maxn 1005
#define MOD 1000000007
#define mem(a , b) memset(a , b , sizeof(a))
#define LL long long
#define INF 100000000
int n;
int a[maxn];
int f[maxn];
int p[maxn];

int gcd(int a , int b)
{
    if(b == 0) return a;
    else return gcd(b , a % b);
}

int main()
{
    int t , tmp , ans ;
    cin >> t;
    p[0] = 1;
    for(int i = 1 ; i <= 1000 ; i ++) p[i] = (p[i-1] << 1) % MOD;
    while(t--)
    {
        mem(f , 0);mem(a , 0);ans = 0;
        cin >> n;
        for(int i = 1 ; i <= n ; i ++) scanf("%d" , &tmp) , a[tmp]++;
        for(int i = 1 ; i <= 1000 ; i ++)
        {
            int t = 0;
            for(int j = i ; j <= 1000 ;j += i) t += a[j];
            f[i] = p[t] - 1;
        }
        for(int i = 1000 ; i > 0 ; i --)
        {
            for(int j = i+i ; j <= 1000 ; j += i) f[i] = (f[i]-f[j] + MOD) % MOD;
            ans = (ans + (LL)1*f[i] * i % MOD) % MOD;
        }
        cout << ans << endl;
    }
    return 0;
}
*/
/*
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <iomanip>

using namespace std;
#pragma comment(linker, "/STACK:102400000,102400000")
//#define maxn 1005
#define MOD 1000000007
#define mem(a , b) memset(a , b , sizeof(a))
#define LL long long
#define ULL unsigned long long
#define INF 100000000
const int maxn = 100000 ;
ULL   base[maxn+8]  ;
const ULL bs = (ULL)27 ;
char  s[maxn + 8] ;
map<ULL , int> mp ;
ULL Hash[maxn + 8] ;

int main(){
    base[0] = 1 ;
    for(int i = 1 ; i <= maxn ; i++)
        base[i] =  base[i-1] * bs ;
    int i , j , n , len , slen , sum   ;
    ULL t ;
    while(scanf("%d%d" , &n , &len) != EOF){
         scanf("%s" ,s) ;
         slen = strlen(s) ;
         Hash[slen] = 0 ;
         for(i = slen-1 ; i >= 0 ; i--)
             Hash[i] = Hash[i+1]*bs + s[i] - 'a' + 1 ;
         sum = 0 ;
         for(i = 0 ; i < len && i+n*len <= slen ; i++){
             mp.clear() ;
             for(j = i ; j < i+n*len ; j += len){
                 t = Hash[j] - Hash[j+len]*base[len] ;
                 mp[t]++ ;
             }
             if(mp.size() == n) sum++ ;
             for(j = i+n*len ; j + len <= slen ; j += len){
                t = Hash[j-n*len] - Hash[j-(n-1)*len]*base[len] ;
                mp[t]-- ;
                if(mp[t] == 0) mp.erase(t) ;
                t = Hash[j] - Hash[j+len]*base[len] ;
                mp[t]++ ;
                if(mp.size() == n) sum++ ;
             }
         }
         printf("%d\n" , sum) ;
    }
    return 0 ;
}
*/
/*
#include <stdio.h>
#include <iostream>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <ctype.h>
#include <time.h>
#include <queue>
#include <iterator>

using namespace std;

int main()
{
	char s[110][110];
	int dp[110][110][2];
	int n, m;

	while (scanf("%d%d", &n, &m) != EOF)
	{
		memset(dp, 0, sizeof(dp));

		for (int i = 1;i <= n;i++)
			cin >> s[i] + 1;
		for (int i = 1;i <= n;i++)
		{
			for (int j = 1;j <= m;j++)
				dp[i][j][0] = dp[i][j][1] = 1e7;
		}

		int cnt = 0 , start = -1;
		for (int i = 1;i <= m;i++)
		{
			if (s[1][i] == 'b') cnt++;
			dp[1][i][1] = cnt;
			dp[1][i][0] = cnt;
			if(cnt && start == -1) start = i-1;
		}

		cnt = 0;


		for (int i = 2;i <= n;i++)
		{
			for (int j = start;j <= m;j++)
			{
				if (s[i][j] == 'b')
				{
					dp[i][j][0] = min(dp[i - 1][j][0], dp[i - 1][j][1]) + 1;
					dp[i][j][1] = min(dp[i][j - 1][1], dp[i][j - 1][0]) + 1;
				}
				else
				{
					dp[i][j][0] = dp[i - 1][j][0];
					dp[i][j][1] = dp[i][j - 1][1];
				}
			}
		}
		cout << endl;
		cout << endl;
		cout << endl;
		for (int i = 1;i <= n;i++)
		{
			for (int j = 1;j <= m;j++)
				printf("%d ", min(dp[i][j][0], dp[i][j][1]));
			cout << endl;
		}
		cout << endl;
		cout << endl;
		cout << endl;
		for (int i = 1;i <= n;i++)
		{
			for (int j = 1;j <= m;j++)
				printf("%d ", dp[i][j][1]);
			cout << endl;
		}
		printf("%d\n", min(dp[n][m][0], dp[n][m][1]));
	}
	return 0;
}*/

/*
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <iomanip>

using namespace std;
#pragma comment(linker, "/STACK:102400000,102400000")
#define maxn 205
#define MOD 1000000007
#define mem(a , b) memset(a , b , sizeof(a))
#define LL long long
const long long INF=0x3fffffff;
int dp[110][110][2];
char a[110][110];

int main()
{
    int n , m;
    while(scanf("%d %d" , &n , &m)!= EOF)
    {
        for(int i = 1 ; i <= n ; i ++)
        {
            scanf("%s" , a[i]+1);
        }
        a[1][1] = '.';
        //cout << a[n][m] << endl;
        if(a[n][m] == 'b')
            dp[n][m][0] = dp[n][m][1] = 1;
        else
            dp[n][m][0] = dp[n][m][1] = 0;
        int cnt = 0;
        if(a[n][m] == 'b') cnt ++;
        for(int i = n-1 ; i >= 1 ; i --)
        {
            if(a[i][m] == 'b') cnt ++;
            dp[i][m][0] = dp[i][m][1] = cnt;
        }
        cnt = 0;
        if(a[n][m] == 'b') cnt ++;
        for(int i = m-1 ; i >= 1 ; i --)
        {
            if(a[n][i] == 'b') cnt ++;
            dp[n][i][0] = dp[n][i][1] = cnt;
        }
        for(int i = n-1 ; i >= 1 ; i --)
        {
            for(int j = m-1 ; j >= 1 ; j --)
            {
                if(dp[i][j + 1][1] > dp[i][j+1][0])   //右边走下一个要转弯
                {
                    if(j+1==m || a[i][j+2] == 'b') dp[i][j][1] = dp[i][j+1][0];
                    else dp[i][j][1] = dp[i][j+1][0] + 1;
                }
                else dp[i][j][1] = dp[i][j+1][1];
                if(dp[i+1][j][0] > dp[i+1][j][1])   //下边走下一个要转弯
                {
                    if(i+1==n || a[i+2][j] == 'b') dp[i][j][0] = dp[i+1][j][1];
                    else dp[i][j][0] = dp[i+1][j][1] + 1;
                }
                else dp[i][j][0] = dp[i+1][j][0];

                if(a[i][j] == 'b') dp[i][j][0]++ , dp[i][j][1] ++;
            }
        }
       // int ans = min(dp[1][1][0] , dp[1][1][1]);
        int ans ;
        if(dp[1][1][0] < dp[1][1][1] && m > 1 && a[1][2] == 'b') ans = dp[1][1][0];
        else ans = dp[1][1][1];
       // if(a[1][1] == 'b') ans --;
       // if(a[n][m] == 'b') ans ++;
        printf("%d\n" , ans);
    }
    return 0;
}
*/
/*
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <iomanip>

using namespace std;
#pragma comment(linker, "/STACK:102400000,102400000")
#define maxn 1000005
#define MOD 1000000007
#define mem(a , b) memset(a , b , sizeof(a))
#define LL long long
const long long INF=0x3fffffff;
int a[maxn] , b[10001];
int Next[10001];

void GetNext(int m)
{
    Next[0] = -1;
    int k = -1 , j = 0;
    while(j < m)
    {
        if(k == -1 || b[j] == b[k])
        {
            k++;
            j++;
            if(b[j] != b[k]) Next[j] = k;
            else Next[j] = Next[k];
        }
        else k = Next[k];
    }
}

int KMP(int n , int m)
{
    int i = 0 , j = 0;
    while(j < m && i < n)
    {
        if(j == -1 || a[i] == b[j])
        {
            i++ , j ++;
        }
        else
        {
            j = Next[j];
        }
    }
    if(j >= m ) return i - m + 1;
    else if(i >= 0) return -1;
}

int main()
{
    int n , m , t;
    cin >> t;
    while(t--)
    {
        scanf("%d %d" , &n , &m);
        for(int i = 0 ; i < n ; i ++) scanf("%d" , &a[i]);
        for(int i = 0 ; i < m ; i ++) scanf("%d" , &b[i]);
        GetNext(m);
        cout << KMP(n , m) << endl;
    }
    return 0;
}
*/

/*
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <iomanip>

using namespace std;
#pragma comment(linker, "/STACK:102400000,102400000")
#define maxn 1000005
#define MOD 1000000007
#define mem(a , b) memset(a , b , sizeof(a))
#define LL long long
#define ULL long long
const long long INF=0x3fffffff;
bool vis[11];
//ofstream  ofile;
int main()
{
    freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    LL n , cas = 1 , t;
    cin >> t;
    while(t--)
    {
        mem(vis , 0);
        scanf("%lld" , &n);
        if(n == 0)
        {
            printf("Case #%lld: INSOMNIA\n" , cas++ );
            continue;
        }
        int tmp = n;
        int num = 0;
        for(int i = 1 ; ;i ++)
        {
            LL tmp = n * i;
            while(tmp)
            {
                if(!vis[tmp%10])
                {
                    vis[tmp%10] = 1;
                    num ++;
                }
                tmp /= 10;
            }
            if(num == 10)
            {
                printf("Case #%lld: %lld\n" , cas++ , n*i);
                break;
            }
        }
    }
    return 0;
}
*/

#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <set>
#include <iomanip>

using namespace std;
#pragma comment(linker, "/STACK:102400000,102400000")
#define maxn 1000005
#define MOD 1000000007
#define mem(a , b) memset(a , b , sizeof(a))
#define LL long long
#define ULL long long
const long long INF=0x3fffffff;
bool vis[11];
char a[105];
//ofstream  ofile;
int main()
{
    freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
    int n , cas = 1 , t;
    cin >> t;
    while(t--)
    {
        mem(vis , 0);
        scanf("%s" , a);
        int len = strlen(a);
        int num = 0;
        for(int i = len - 1; i >= 0 ; i --)
        {
            if(a[i] == '+') continue;
            else
            {
                num ++;
                for(int j = i ; j >= 0 ; j --)
                {
                    if(a[j] == '+') a[j] = '-';
                    else a[j] = '+';
                }
            }
        }
        printf("Case #%d: %d\n" , cas++ , num);
    }
    return 0;
}
