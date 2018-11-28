//AUTOR:MURRUGARRA LLERENA JEFFRI
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
   freopen("A-large.in", "r", stdin);
   freopen("A-large.txt", "w", stdout);
*/
int casos;
lli n;
scanf("%d",&casos);
REP(i,casos)
{
    int val[10]={0};
    scanf("%lld",&n);
    if(n==0)
        printf("Case #%d: INSOMNIA\n",i+1);
    else
    {
        int cont=10;
        lli j=1;
        while(cont!=0)
        {
            lli num2=n*j;
            lli num=num2;
            while(num!=0)
            {
                lli num1=num%10;
                    if(val[num1]==0)
                        {

                            val[num1]=1;
                            cont--;
                            if(cont==0)
                                printf("Case #%d: %d\n",i+1,num2);
                        }
                num/=10;
            }
            j++;
        }
    }
}
/*
    fclose(stdin);
    fclose(stdout);
*/

    return 0;
}


