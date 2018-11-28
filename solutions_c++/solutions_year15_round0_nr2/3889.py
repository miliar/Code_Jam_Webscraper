

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
#define inf_i (1<<30)-1

int main(){
/*
   freopen("input2.in", "r", stdin);
   freopen("out2.txt", "w", stdout);
*/
    int test,x,time,n,acu[1005],acu2[1005];
    scanf("%d",&test);
    REP(t,test)
    {
        scanf("%d",&n);
        mset(acu,0);
        mset(acu2,0);
        time=0;
        REP(i,n)
            scanf("%d",&x),time=max(x,time),acu[x]++,acu2[x]++;

        int st=0,temp;
        RFOR(i,1000,2)
        {
            if(acu[i])
            {
                time=min(time,st+i);
                st+=acu[i];
                temp=acu[i];
                acu[i]=0;
                int add1=i/2,add2=i-i/2;
                acu[add1]+=temp;
                acu[add2]+=temp;
            }
        }
        st=0;
        RFOR(i,1000,2)
        {
            if(acu2[i])
            {
                time=min(time,st+i);
                st+=acu2[i];
                temp=acu2[i];
                acu2[i]=0;
                int add1=i/2,add2=i-i/2;
                if(add2&1 && i&1)
                    add2++,add1--;
                acu2[add1]+=temp;
                acu2[add2]+=temp;
            }
        }
        printf("Case #%d: %d\n",t+1,time);
    }
/*
    fclose(stdin);
    fclose(stdout);
*/

    return 0;
}


