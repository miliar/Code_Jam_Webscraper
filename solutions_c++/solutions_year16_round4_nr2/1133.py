#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
double p[256], a[256][256];

double solve(const vector<double>& u, const int n, const int m)
{
    double& ans=a[n][m];
    
    if( ans<0 )
    {
        ans=0;
        
        if( m==0 )
            ans= n==0 ? 1 : solve(u, n-1, 0)*(1-u[n-1]);
        else if( n==0 )
            ans=0;
        else if( n>=m )
            ans=solve(u, n-1, m)*(1-u[n-1])+solve(u, n-1, m-1)*u[n-1];
    }
    
    return ans;
}

void solve(double& ans, vector<double>& u, int n, int k)
{
    if( k==0 )
    {
        for(int i=u.size(); i>=0; i--)
            for(int j=u.size(); j>=0; j--)
                a[i][j]=-1;
        
        ans=max(ans, solve(u, u.size(), u.size()>>1));
    }
    else if( n<k )
        return ;
    else
    {
        solve(ans, u, n-1, k);
        u.push_back(p[n-1]);
        solve(ans, u, n-1, k-1);
        u.pop_back();
    }
}

int main()
{
    int N;
    scanf("%d", &N);
    
    for(int cases=1; cases<=N; cases++)
    {
        int n, m;
        scanf("%d%d", &n, &m);
        
        for(int i=0; i<n; i++)
            scanf("%lf", &p[i]);
        
        double ans=0;
        vector<double> u;
        solve(ans, u, n, m);
        printf("Case #%d: %f\n", cases, ans);
    }
}