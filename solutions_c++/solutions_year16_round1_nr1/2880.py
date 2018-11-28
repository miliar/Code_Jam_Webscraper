#include <bits/stdc++.h>
using namespace std;
#define li long long int
#define rl(n) scanf("%lld", &n)
#define rll(m,n) scanf("%lld %lld", &m, &n)
#define rlll(m,n,o) scanf("%lld %lld %lld", &m, &n, &o)
#define ri(n) scanf("%d", &n)
#define rc(n) scanf("%c", &n)
#define rs(n) gets(s)
#define rst(n) getline(cin,n)
#define rfile(a) freopen(a, "r", stdin)
#define pi acos(-1.00)
#define pb push_back
#define mp make_pair
#define Pr printf
#define For(i,a,b) for(int i = a; i < b; i++)
#define MOD 1000003
#define eps 1e-9
#define ru(n) scanf("%llu",&n)
#define ruuu(m,n,o) scanf("%llu %llu %llu", &m, &n, &o)
#define ui unsigned long long int
li facs[1000001];

li inv_modulo(li a, li b)
{
	li b0 = b, t, q;
	li x0 = 0, x1 = 1;
	if (b == 1) return 1;
	while (a > 1) {
		q = a / b;
		t = b, b = a % b, a = t;
		t = x0, x0 = x1 - q * x0, x1 = t;
	}
	if (x1 < 0) x1 += b0;
	return x1;
}

void factorial()
{
    li n = 1000000;
    facs[1] = 1;
    facs[0] = 0;
    li fac = 1;
    for(li i = 2; i <= n; i++)
    {
        fac = (fac*i) % MOD;
        facs[i] = fac;
    }
}

string preProcess(string s) {
  int n = s.length();
  if (n == 0) return "^$";
  string ret = "^";
  for (int i = 0; i < n; i++)
    ret += "#" + s.substr(i, 1);

  ret += "#$";
  return ret;
}

string longestPalindrome(string s)
{
        string T = preProcess(s);
        int n = T.length();
        int *P = new int[n];
        int C = 0, R = 0;
        for (int i = 1; i < n-1; i++)
        {
            int i_mirror = 2*C-i; // equals to i' = C - (i-C)

            if(R > i)
            {
                P[i] = min(R-i, P[i_mirror]);
            }
            else{
                P[i] = 0;
            }
            // Attempt to expand palindrome centered at i
            while (T[i + 1 + P[i]] == T[i - (1 + P[i])])
            {
                P[i]++;
            }

            // If palindrome centered at i expand past R,
            // adjust center based on expanded palindrome.
            if (i + P[i] > R)
            {
                C = i;
                R = i + P[i];
            }
        }

        // Find the maximum element in P.
        int maxLen = 0;
        int centerIndex = 0;
        for (int i = 1; i < n-1; i++)
        {
            if (P[i] > maxLen)
            {
                maxLen = P[i];
                centerIndex = i;
            }
        }
        int start = (int) (centerIndex - 1 - maxLen)/2.00;
        int fin = maxLen;
        return s.substr(start, fin);
}

li bigmod(li a, li b, li M)
{
    if(b == 0) return 1;
    li x = bigmod(a,b/2,M);
    x = (x*x) % M;
    if((b&1) == 1) x = (x*a) % M;
    return x;
}
template <typename t1> t1 gcd(t1 a, t1 b) { return b == 0 ? a : gcd(b, a % b); }
template <typename t1> t1 lcm(t1 a, t1 b) { return a * (b / gcd(a, b)); }
template <typename t1> bool check (t1 i, t1 k){return i&((t1)1<<k);}
template <typename t1> t1 On(t1 i, t1 k) { return i|((t1)1 << k);}
template <typename t1> t1 Off(t1 i, t1 k) {return (i-((check(i,k))<<k) );}

int gray_to_int(int n)
{
    int lm = -1;
    int binary = 0;
    for(int i = 31; i >= 0; i--)
    {
        if(check(n,i) == 1)
        {
            lm = i;
            break;
        }
    }
    if(lm == -1) return 0;

    binary = On(binary, lm);

    for (int i = lm-1; i >= 0; i--)
    {
        bool ck = check(n, i);
        bool prev = check(binary, i + 1);

        if (ck == 0 && prev == 0)
        {
            binary = Off(binary, i);
        }
        else if (ck == 1 && prev == 1)
        {
            binary = Off(binary,i);
        }
        else if (ck == 0 && prev == 1)
        {
            binary = On(binary,i);
        }
        else if (ck == 1 && prev == 0)
        {
             binary = On(binary,i);
        }
      }
      return binary;
}
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d ", &t);
    For(tc,1,t+1)
    {
        char arr[1200]; scanf("%s", arr);
        string s(arr);
        int ln = s.length();
        deque<char> wd;
        wd.push_back(s[0]);
        for(int i = 1; i < ln; i++)
        {
            if(s[i] >= wd.front())
            {
                wd.push_front(s[i]);
            }
            else wd.push_back(s[i]);
        }

        printf("Case #%d: ", tc);
        char x;
        while(wd.empty() == false)
        {
            x = wd.front();
            wd.pop_front();
            printf("%c",x);
        }
        printf("\n");
    }
    return 0;
}
