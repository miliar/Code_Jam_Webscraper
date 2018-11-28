#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>

using namespace std;

#define DEBUG  //comment this line to pull out print statements
#ifdef DEBUG
#define TAB '\t'
#define debug(a, end) cout << #a << ": " << a << end
#define dbg(end) end
#else
#define debug(a, end)
#define dbg(end)
#endif

typedef pair<int, int> point;
typedef vector<int> vi;
typedef vector<point> vp;

#define UN(v) SORT(v),v.erase(unique(v.begin(),v.end()),v.end())   
#define SORT(c) sort((c).begin(),(c).end())   
#define FOR(i,a,b) for (int  i=(a); i < (b); i++)    
#define REP(i,n) FOR(i,0,(int)n)    
#define CL(a,b) memset(a,b,sizeof(a))
#define CL2d(a,b,x,y) memset(a, b, sizeof(a[0][0])*x*y)

/*global variables*/
char S[110];
/*global variables*/

void dump()
{
    //dump data
}

bool getInput()
{
    //get input
    fgets(S, 110, stdin);
    S[strlen(S)-1] = 0;
    return true;
}

int cpos()
{
    int tot = 0;
    for(int i = 0; i < strlen(S); ++i)
        if (S[i] == '+') tot++;

    return tot;
}

void flip(char* c)
{
    switch (*c)
    {
    case '+':
        *c = '-';
        break;
    case '-':
        *c = '+';
        break;
    }
}

void process()
{
    //process input
    char cur = S[0];
    int cnt = 0;
    //debug(cur, TAB); debug(S, TAB); debug(cpos(), endl);
    while (cpos() != strlen(S))
    {
        for (int i = 0; i < strlen(S); ++i)
        {
            if (S[i] == cur)
                flip(&S[i]);
            else
                break;
        }
        cur = S[0];
        ++cnt;
    }
    printf("%d\n", cnt);
}

int main()
{
    int nc;
    int cn = 1;
    scanf("%d ", &nc);
    while (nc-- > 0)
    {
        printf("Case #%d: ", cn++);
        getInput();
        process();

        /*CLEAR GLOBAL VARIABLES!*/

        /*CLEAR GLOBAL VARIABLES!*/
    }

    return 0;
}
