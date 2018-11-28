#include <bits/stdc++.h>
#define MOD 1000000007

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef pair<string,string> ss;

int n,k;
double p[210];

int main()
{
    ifstream fin("input.in");
    ofstream fout("output.out");
    int t;
    fin >> t;
    int T=t;
    fout<<setprecision(10)<<fixed;
    while(t--)
    {
        fout<<"Case #"<<T-t<<": ";
        double rez=0;
        fin>>n>>k;
        for(int ctr1=0;ctr1<n;ctr1++)
            fin>>p[ctr1];
        sort(p,p+n);
        for(int ctr1=0;ctr1<n;ctr1++)
            p[n+ctr1]=p[ctr1];
        for(int ctr1=0;ctr1<2*n-k;ctr1++){
            double dp[k+1][k+1];
            for(int ctr2=0;ctr2<=k;ctr2++)
                for(int ctr3=0;ctr3<=k;ctr3++)
                    dp[ctr2][ctr3]=0;
            dp[0][0]=1;
            for(int ctr2=1;ctr2<=k;ctr2++){
                for(int ctr3=0;ctr3<k;ctr3++){
                    dp[ctr2][ctr3]+=(dp[ctr2-1][ctr3])*(1-p[ctr1+ctr2-1]);
                    if(ctr3>0)
                        dp[ctr2][ctr3]+=(dp[ctr2-1][ctr3-1])*(p[ctr1+ctr2-1]);
                }
            }
            rez=max(rez,dp[k][k/2]);
        }
        fout<<rez<<"\n";
    }
    fin.close();
    fout.close();
    return 0;
}


/*

#include <bits/stdc++.h>
#define MOD 1000000007

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;
typedef pair<string,string> ss;

int n,k;
double p[210];
double cp[210][2];

void dfs(int l,int r,int bm,int ar){
    if((1<<l)&&bm){
        for(int ctr1=0;ctr1<n;ctr1++)
            if()
    }
    dfs(l+1,r,bm,ar);
}

int main()
{
    ifstream fin("input.in");
    ofstream fout("output.out");
    int t;
    fin >> t;
    int T=t;
    fout<<setprecision(10)<<fixed;
    while(t--)
    {
        fout<<"Case #"<<T-t<<": ";
        fin>>n>>k;
        for(int ctr1=0;ctr1<n;ctr1++)
            fin>>p[ctr1];
        int bm=1<<(n-1);
        for(int ctr1=0;ctr1<bm;ctr1++)
        if(__builtin_popcount(bm)==k){
            for(int ctr1=0;ctr1<n;ctr1++)
            cp[ctr1][0]=cp[ctr1][1]=0;
            cp[0][0]=cp[1][0]=1;
            dfs(0,(n+1)/2,0);
            dfs((n+1)/2,n,1);

        }


    }
    fin.close();
    fout.close();
    return 0;
}

*/
