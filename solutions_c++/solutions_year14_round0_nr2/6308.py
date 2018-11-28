#include <bits/stdc++.h>
#define REP(i, a) for( int i = 0; i < a; i++ )
#define RFOR(i,x,y) for(int i = x; i>= y; i--)
#define FOR(i,x,y) for (int i = x; i <= y; i++)
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

using namespace std;

#define ll long long
#define MAX 20005

int main(){

  freopen("B-large.in", "r", stdin);
  freopen("Large.txt", "w", stdout);
    int test,cases; double C, F, X, cps, t, tmax1, tmax2, temp;
    bool band;
    scanf("%d",&test);
    REP(cases,test)
    {
        cps = (double)2; band = true; t = 0;

        scanf("%lf %lf %lf", &C, &F, &X);
        if( cps == X )
        {
            band = false;
            printf("Case #%d: %.7lf\n",cases+1, (double)X / (double)cps );
        }
        else
            tmax1 = X / cps;
        while( band )
        {
            t += (C / cps); cps+= F;
            tmax2 = t +  ( X / cps );
            //cout<< t << " " << cps << " " << tmax1 << " " << tmax2 <<endl;

            if(tmax2 >= tmax1 )
            {
                printf("Case #%d: %.7lf\n",cases+1, tmax1);
                band = false;
            }
            else
            {
                temp = tmax1;
                tmax1 = tmax2;
                tmax2 = temp;
            }
        }
    }

  fclose(stdin);
  fclose(stdout);

    return 0;
}
