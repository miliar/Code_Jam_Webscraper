   /* ******************************************************
   *  Md. Abdulla-Al-Sun
   *  Codeforces: sun.  , Topcoder : sun.
   *  Uva: sun. , SPOJ : sun_kuet  , LOJ : 5002 CodeChef: sun_kuet
   *  KUET, Bangladesh
   ****************************************************** */

#include <bits/stdc++.h>
#define scan(a) scanf("%d",&a)
#define rep0(i,n) for(int i = 0; i<n ;i++)
#define rep1(i,n) for(int i = 1; i<=n ;i++)
#define rep(i,a,b) for(int i = a; i<=b ;i++)
#define READ() freopen("input.txt","r",stdin);
int setbit(int N,int pos) { return N = N|(1<<pos); }
int resetbit(int N, int pos){ return N = N & ~(1<<pos) ;}
bool checkbit(int N,int pos) { return (bool) (N & 1<<pos) ;}
#define LL long long int
#define mx 15
#define MAX 15
using namespace std;

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("A-large.out", "w", stdout);

    string s;
    int n;
    int test;
    cin >> test;
    for(int t = 1; t <= test ; t ++ )
    {
        cin >> n >> s;
        int cnt = 0 , sum = 0;
        int ln  = s.size();
        for(int i = 0; i< ln; i++ )
        {
            sum += (int)(s[i]-'0');
            if(sum < (i+1))
            {
                cnt ++;
                sum ++;
            }
        }
        printf("Case #%d: %d\n",t,cnt);
    }
}
