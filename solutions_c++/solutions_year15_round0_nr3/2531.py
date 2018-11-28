

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

int qua[6][6]=  {
                 {0,0,0,0,0},
                 {0,1,2,3,4},
                 {0,2,-1,4,-3},
                 {0,3,-4,-1,2},
                 {0,4,3,-2,-1},
                };

int main(){
/*
   freopen("input1.in", "r", stdin);
   freopen("out1.txt", "w", stdout);
*/
    int test,l,x;
    string cad;
    scanf("%d",&test);
    REP(t,test)
    {
        scanf("%d %d",&l,&x);
        cin.ignore();
        getline(cin,cad);
        string cadena="";
        REP(i,x)
            cadena+=cad;
        if(l*x<3)
            printf("Case #%d: NO\n",t+1);
        else
        {
            int left[10005],right[10005];
            VE IS,JS;
            //izq-der
            left[0]=cadena[0]-'h'+1;
            if(left[0]==2)
                    IS.PB(0);
            FOR(i,1,l*x)
            {
                int idx_i=left[i-1],idx_j=cadena[i]-'h'+1,neg=1;
                if(idx_i<0)
                    neg=-1,idx_i*=-1;
                left[i]=qua[idx_i][idx_j]*neg;
                if(left[i]==2)
                    IS.PB(i);
            }
            //der-izq
            right[l*x-1]=cadena[l*x-1]-'h'+1;
            if(right[l*x-1]==4)
                    JS.PB(l*x-1);
            RFOR(i,l*x-2,0)
            {
                int idx_i=right[i+1],idx_j=cadena[i]-'h'+1,neg=1;
                if(idx_i<0)
                    neg=-1,idx_i*=-1;
                right[i]=qua[idx_j][idx_i]*neg;
                if(right[i]==4)
                    JS.PB(i);
            }

            bool sol=false;
            REP(i,IS.size())
            {
                REP(j,JS.size())
                {
                    if(IS[i]+1<=JS[j]-1 && right[IS[i]+1]==2 && left[JS[j]-1]==4)
                    {
                        sol=true;
                        break;
                    }
                }
            }
            printf("Case #%d: %s\n",t+1,(sol?"YES":"NO"));
        }
    }
/*
    fclose(stdin);
    fclose(stdout);
*/

    return 0;
}


