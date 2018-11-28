#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

FILE *f, *g;
int dp[1000100];
int t[1000100];
int st[11];
int cnt[11];
int dig[11];
int bf[11],cn,cif;


int inverse(int x)
{
     int res= 0;
     while (x)
     {
        res = res*10+x%10;
        x/=10;
     }
    return res;
}

void pre()
{
    queue <int> Q;
	dp[1] = 1;
	int i,k,j;

    for (i=1;i<=1000000;i++)
    {
        dp[i] = i;
        t[i] = i-1;
    }
    Q.push(1);

	for (i = 2; i <= 1000000; i++)
	{
        if (dp[i+1]>dp[i]+1)
        {
            t[i+1] = i;
            dp[i+1] = dp[i]+1;
        }

        int inv = inverse(i);

        if (dp[inv]>dp[i]+1)
        {
            t[inv] = i;
            dp[inv] = dp[i]+1;
        }
	}
}
int T;

int brut(long long X)
{
    int res = 1;
    long long pas = 1;

    while (pas< X)
    {


    }


}

void rec(int x)
{
    vector <int> s;
    while (x!=0 )
    {
        s.push_back(x);
        x = t[x];
    }
    for (int i=s.size()-1;i>=0;i--)
        fprintf(g,"%d ",s[i]);
}


int main()
{
	f = fopen("input.txt", "r");
	g = fopen("output.txt", "w");
	fscanf(f,"%d", &T);

    pre();


	for (int q=1;q<=T;q++)
	{
		int n;
		fscanf(f,"%d", &n);
		fprintf(g,"Case #%d: %d\n",q, dp[n]);
	}

	return 0;
}
