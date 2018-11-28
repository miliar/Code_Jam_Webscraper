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
#define inf_i 1<<30-1

int main(){
/*
   freopen("input.txt", "r", stdin);
   freopen("out.txt", "w", stdout);
*/
    int test,freq[20],x,c;
    scanf("%d",&test);
    REP(t,test)
    {
        scanf("%d",&c);
        mset(freq,0);
        REP(i,4)
        {
            REP(j,4)
            {
                scanf("%d",&x);
                if(i==c-1)
                    freq[x]++;
            }
        }

        scanf("%d",&c);
        REP(i,4)
        {
            REP(j,4)
            {
                scanf("%d",&x);
                if(i==c-1)
                    freq[x]++;
            }
        }
        int cnt=0,sol=-1;
        FOR(i,1,17)
            if(freq[i]==2)
                cnt++,sol=i;
        printf("Case #%d: ",t+1);
        if(cnt==0)
            printf("Volunteer cheated!\n");
        else if(cnt>1)
            printf("Bad magician!\n");
        else
            printf("%d\n",sol);
    }

/*
    fclose(stdin);
    fclose(stdout);
*/
    return 0;

}


