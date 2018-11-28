#include<iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <list>


#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
#include <cctype>


using namespace std;

typedef long long int lli;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair < int, int > pii;
typedef vector< pii > vii;

#define PI (2*acos(0))
#define EPS 1e-9
#define PB push_back
#define MAX max_element
#define MIN min_element
#define BS binary_search
#define MP make_pair
#define LN length()
#define SZ size()

#define ASZ(x) sizeof(x)/sizeof(__typeof(x[0]))
#define ALL(x) x.begin(), x.end()
#define LC(x,y) lexicographical_compare(ALL(x),ALL(y))
#define REP(i,n) for(int i=0, _e(n); i<_e; i++)
#define FOR(i,a,b) for(int i(a), _e(b); i<=_e; i++)
#define FORD(i,a,b) for(int i(a), _e(b); i>=_e; i--)
#define FORIT(i, m) for (__typeof((m).begin()) i=(m).begin(); i!=(m).end(); ++i)
#define SET(t,v) memset((t), (v), sizeof(t))
#define UNIQUE(c) (c).resize( unique( ALL(c) ) - (c).begin() )
#define F first
#define S second

pair<set<int>::iterator,bool> RET;// for checking if the item has been aded to a set or not

char board[4][4];

void print()
{
    printf("\n");
    REP(i,4)
    {
        REP(j,4)
        {
            printf("%c",board[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

string result()
{
    bool t,o,x,d,ic;
    ic=false;

    // Horizontal check

    REP(i,4)
    {
        t=o=x=d=false;
        REP(j,4)
        {
            if(board[i][j]=='T')
            {
                t=true;
            }
            else if(board[i][j]=='O')
            {
                o=true;
            }
            else if(board[i][j]=='X')
            {
                x=true;
            }
            else
            {
                d=ic=true;
            }
        }
        if(d)continue;
        if(x&&(!o))
        {
            return "X won";
        }
        if(o&&(!x))
        {
            return "O won";
        }
    }

    //cerr<<"horizontal check finished\n";
    //Vertical Check

    REP(j,4)
    {
        t=o=x=d=false;
        REP(i,4)
        {
            if(board[i][j]=='T')
            {
                t=true;
            }
            else if(board[i][j]=='O')
            {
                o=true;
            }
            else if(board[i][j]=='X')
            {
                x=true;
            }
            else
            {
                d=ic=true;
            }
        }
        if(d)continue;
        if(x&&(!o))
        {
            return "X won";
        }
        if(o&&(!x))
        {
            return "O won";
        }
    }
    //cerr<<"vertical check finished\n";
    //Diagonal check
    t=o=x=d=false;
    REP(i,4)
    {
        if(board[i][i]=='T')
        {
            t=true;
        }
        else if(board[i][i]=='O')
        {
            o=true;
        }
        else if(board[i][i]=='X')
        {
            x=true;
        }
        else
        {
            d=ic=true;
        }
    }

    if(x&&(!o)&&(!d))
    {
        return "X won";
    }
    if(o&&(!x)&&(!d))
    {
        return "O won";
    }

    t=o=x=d=false;
    REP(i,4)
    {
        if(board[i][3-i]=='T')
        {
            t=true;
        }
        else if(board[i][3-i]=='O')
        {
            o=true;
        }
        else if(board[i][3-i]=='X')
        {
            x=true;
        }
        else
        {
            d=ic=true;
        }
    }

    if(x&&(!o)&&(!d))
    {
        return "X won";
    }
    if(o&&(!x)&&(!d))
    {
        return "O won";
    }

    if(ic){
        return "Game has not completed";
    }

    return "Draw";
}

int main()
{
#ifdef _orfi_
    freopen("A-small-attempt0.in","rt",stdin);
    freopen("A-small-attempt0.out","wt",stdout);
#endif
    int T,cas=0;
    scanf("%d\n",&T);
    while(T--)
    {
        REP(i,4)
        {
            REP(j,4)
            {
                scanf("%c",&board[i][j]);
            }
            scanf("\n");
        }
        scanf("\n");
        printf("Case #%d: ",++cas);
        cout<<result()<<endl;
    }

    return 0;
}



