#include <bits/stdc++.h>

using namespace std;

const int nmax = 19;

int n , k , test , T , i;
double yes[nmax] , no[nmax] , dp[1 << nmax];
double answer;

void bkt(int step , int p , int mask , int nryes , double prob)
{
    if (step == n)
    {
        if (p == k && nryes == k / 2)
        dp[mask] += prob;

        return;
    }

    bkt(step + 1 , p , mask , nryes , prob);
    bkt(step + 1 , p + 1 , mask + (1 << step) , nryes + 1 , prob * yes[step]);
    bkt(step + 1 , p + 1 , mask + (1 << step) , nryes , prob * no[step]);
}

int main()
{
freopen("test.in" , "r" , stdin);
freopen("test.out" , "w" , stdout);

cin >> T;

for (test = 1 ; test <= T ; ++test)
{
    cin >> n >> k;

    for (i = 0 ; i < n ; ++i)
    cin >> yes[i] , no[i] = 1.0 - yes[i];

    answer = 0.0;
    bkt(0 , 0 , 0 , 0 , 1.0);

    for (i = 0 ; i < (1 << n) ; ++i)
    {
        answer = max(answer , dp[i]);
        dp[i] = 0.0;
    }

    cout << "Case #" << test << ": ";
    cout << fixed << setprecision(10) << answer << '\n';
}


return 0;
}
