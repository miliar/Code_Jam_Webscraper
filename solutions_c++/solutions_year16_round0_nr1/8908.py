#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <map>
#include <sstream>
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
map<char, int> seen;
int N;
/*global variables*/

void dump()
{
    //dump data
}

bool getInput()
{
    //get input
    scanf("%d ", &N);
    return true;
}

void process()
{
    //process input
    long long i = N;
    long long j = 0;
    string num;
    stringstream sstr;
    for (; i > j;)
    {
        sstr.clear();
        sstr << i;
        sstr >> num;
        //debug(num, endl);
        for (int k = 0; k < num.length(); ++k)
        {
            seen[num[k]]++;
        }
        if (seen.size() == 10) break;
        j = i;
        i += N;
    }
    if (seen.size() == 10)
        printf("%lld", i);
    else
        printf("INSOMNIA");
    puts("");
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
        seen.clear();
        /*CLEAR GLOBAL VARIABLES!*/
    }

    return 0;
}
