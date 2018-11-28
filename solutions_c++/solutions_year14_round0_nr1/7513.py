#include <bits/stdc++.h>

#define ALL(c)        c.begin(), c.end()
#define TR(c, it)     for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define FOR(i, j, n)  for(int (i) = (j); i < n; i++)
#define REP(i, j, lo) for(int (i) = (j); i >= (lo); i--)
#define MAX(a, b)     ((a) > (b) ? (a) : (b))
#define MIN(a, b)     ((a) < (b) ? (a) : (b))
#define gc            getchar_unlocked
#define pu            putchar_unlocked

#ifndef ONLINE_JUDGE
    #define gc getchar
#endif

#define ll            long long int
#define ull           unsigned long long int
#define inf           INT_MAX
#define mininf        INT_MIN
#define pb            push_back
#define pob           pop_back
#define pf            push_front
#define pof           pop_front
#define mp            make_pair
#define PI            3.14159265358979323846264338327950288
#define endl          '\n'
#define SET(arr, val) memset(arr, val, sizeof arr)
#define SI            ( { int x; scanf("%d", &x); x; } )
#define IOSFAST       ( ios::sync_with_stdio(false); )
#define mod           1000000
#define SIZE          500000
inline void MAXR(int &a, int b){ if(a < b)   a = b; }
#define pi pair<int , int >

using namespace std;

int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("output1.out", "w", stdout);
    int t = SI , p = 0;
    FOR(p , 0 , t)
    {
        int card1[4][4] , q1 = SI ;
        q1--;
        FOR(i , 0 , 4)
            FOR(j , 0 , 4)
                card1[i][j] = SI;
        int card2[4][4] , q2 = SI;
        q2--;
        FOR(i , 0 , 4)
            FOR(j , 0 , 4)
                card2[i][j] = SI;
        int same = 0 , num;
        FOR(i , 0 ,4)
            FOR(j , 0 , 4)
                if(card1[q1][i] == card2[q2][j])
                    same++ , num = card2[q2][j];
        printf("Case #%d: ",p+1);
        if(same == 0)
            printf("Volunteer cheated!\n");
        else if(same > 1)
            printf("Bad magician!\n");
        else if(same == 1)
            printf("%d\n",num);
    }
}
