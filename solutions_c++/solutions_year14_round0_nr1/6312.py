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

  //freopen("A-small-attempt0.in", "r", stdin);
  //freopen("out.txt", "w", stdout);
    int test, fil, fil2,num; VE vecA,vecB;
    scanf("%d",&test);
    REP(cases,test)
    {
        scanf("%d",&fil);
        REP(I,16)
        {
            scanf("%d",&num);
            if( I>=(fil-1)*4  && I<(fil*4))
                vecA.PB(num);
        }

        scanf("%d",&fil2);
        REP(I,16)
        {
            scanf("%d",&num);
            if( I>=(fil2-1)*4  && I<(fil2*4))
                vecB.PB(num);
        }

        sort(all(vecB));
        int cont=0, temp;
        REP(I,4)
        {
            if(binary_search(all(vecB),vecA[I])){
                cont++;
                temp = vecA[I];
            }
        }

        if(cont == 1)
            printf("Case #%d: %d\n",cases+1,temp);
        if(cont == 0)
            printf("Case #%d: Volunteer cheated!\n",cases+1);
        if(cont > 1)
            printf("Case #%d: Bad magician!\n",cases+1);


        vecA.clear(); vecB.clear();

    }

  //fclose(stdin);
  //fclose(stdout);

    return 0;
}
