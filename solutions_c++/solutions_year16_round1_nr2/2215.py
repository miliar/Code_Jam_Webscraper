//AUTOR:MURRUGARRA JEFFRI ERWIN
//UNIVERSIDAD: UNIVERSIDAD NACIONAL DE TRUJILLO
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
   freopen("B-large (1).in", "r", stdin);
   freopen("B-large (1).txt", "w", stdout);
*/
int casos,n;
scanf("%d",&casos);
REP(i,casos)
{
    vector<int>re;
    int freq[2501]={0};
    scanf("%d",&n);
    int num;
    REP(i,(n*2)-1)
    {
        REP(j,n)
        {
            scanf("%d",&num);
            freq[num]++;
        }
    }
    REP(i,2501)
    {
        if(freq[i]&1==1)
            re.push_back(i);
            sort(re.begin(),re.end());

    }
    printf("Case #%d:",i+1);
    REP(i,re.size())
    {
        printf(" %d",re[i]);
    }
    printf("\n");
    re.clear();
}

/*
    fclose(stdin);
    fclose(stdout);

*/
    return 0;
}



