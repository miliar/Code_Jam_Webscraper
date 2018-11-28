#include <bits/stdc++.h>
using namespace std;

int t;

int n, k;

double tab[207];

double wyn;
double aktu;

vector <double> tak, nie;

double dp[207][207];

int p1, p2;
double p3;

int l;

inline double licz()
{
    for (int i=0; i<=k; i++)
    {
        for (int j=0; j<=k/2; j++)
        {
            dp[i][j]=0.0;
        }
    }
    dp[0][0]=1.0;
    for (int i=0; i<k; i++)
    {
        for (int j=0; j<=k/2; j++)
        {
            dp[i+1][j]+=dp[i][j]*(1.0-tak[i]);
            dp[i+1][j+1]+=dp[i][j]*tak[i];
        }
    }
    return dp[k][k/2];
}

int main()
{
    srand(time(0));
    scanf("%d", &t);
    for (int tt=1; tt<=t; tt++)
    {
        printf("Case #%d: ", tt);
        scanf("%d%d", &n, &k);
        for (int i=1; i<=n; i++)
        scanf("%lf", &tab[i]);
        random_shuffle(tab+1, tab+1+n);
        tak.clear();
        nie.clear();
        for (int i=1; i<=k; i++)
        {
            tak.push_back(tab[i]);
        }
        for (int i=k+1; i<=n; i++)
        {
            nie.push_back(tab[i]);
        }
        aktu=licz();
        wyn=aktu;
        l=0;
        if (k!=n)
        {
            for (int h=1; h<=1000000; h++)
            {
                p1=rand()%k;
                p2=rand()%(n-k);
                swap(tak[p1], nie[p2]);
                p3=licz();
                if (p3>aktu || l>1000)
                {
                    aktu=p3;
                    l=0;
                }
                else
                {
                    swap(tak[p1], nie[p2]);
                    l++;
                }
                wyn=max(wyn, aktu);
            }
        }
        printf("%.9lf\n", wyn);
    }
    return 0;
}
