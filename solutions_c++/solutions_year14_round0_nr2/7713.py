#include <bits/stdc++.h>

#define REP(i, a) for( int i = 0; i < a; i++ )
#define RFOR(i,x,y) for(int i = x; i>= y; i--)
#define FOR(i,x,y) for (int i = x; i < y; i++)
#define ITFOR(it,A) for(typeof A.begin() it = A.begin(); it!=A.end(); it++)
#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define VE vector <int>
#define mset(A,x) memset(A, x, sizeof A)
#define PB push_back
#define ones(x) __builtin_popcount(x)
#define cua(x) (x)*(x)
#define debug(x) cout <<#x << " = " << x << endl
#define adebug(x,n) cout <<#x<<endl; REP(i,n)cout<<x[i]<<char(i+1==n?10:32)
#define mdebug(x,m,n) cout <<#x<<endl; REP(i,m)REP(j,n)cout<<x[i][j]<<char(j+1==n?10:32)
#define LSOne(S) (S&(-S))

using namespace std;

#define ll long long
#define lli long long int
#define PI acos(-1.0)
#define ii pair<int,int>
#define inf_ll (((1LL<<62)-1)<<1)+1
#define inf_i (1<<30-1)

double menor(double x,double y)
{
    return (x<y)?x:y;
}
int main(){
/*
   freopen("B-small-attempt3.in", "r", stdin);
   freopen("out3.txt", "w", stdout);
*/
    static double arr[50000005];
    int test;
    double c,f,x;
    scanf("%d",&test);
    REP(t,test)
    {
        scanf("%lf %lf %lf",&c,&f,&x);
        int ind=0;
        for(double i=2.0;i<c*100000+1;i+=f)
            arr[ind++]=c/i;
        FOR(i,1,ind)
            arr[i]+=arr[i-1];
        double sol=x/2.0,aux;
        REP(i,ind)
        {
            sol=menor(sol,arr[i]+x/(2.0+f*(i+1)));
            //cout<<arr[i]+x/(2.0+f*(i))<<"   ";
        }
        //cout<<endl;
        printf("Case #%d: %.7llf\n",t+1,sol);
    }
/*
    fclose(stdin);
    fclose(stdout);
*/
    return 0;

}


