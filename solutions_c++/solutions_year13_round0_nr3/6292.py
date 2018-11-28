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
typedef vector<int> vi; //?
typedef vector<point> vp; //?

#define UN(v) SORT(v),v.erase(unique(v.begin(),v.end()),v.end())   
#define SORT(c) sort((c).begin(),(c).end())   
#define FOR(i,a,b) for (int  i=(a); i < (b); i++)    
#define REP(i,n) FOR(i,0,n)    
#define CL(a,b) memset(a,b,sizeof(a))
#define CL2d(a,b,x,y) memset(a, b, sizeof(a[0][0])*x*y)

/*global variables*/
int first, second;
map<int, bool> fas;
/*global variables*/

void dump()
{
    //dump data
}

bool getInput()
{
    //get input
    scanf("%d %d", &first, &second);
    return true;
}

bool ispalindrome(long long s)
{
    string r;
    stringstream sstr;
    sstr << s;
    sstr >> r;
    string x = r;
    reverse(r.begin(), r.end());
    if (x.compare(r) == 0) return true;
    return false;
}

void process()
{
    //process input
    int total = 0;
    FOR(i, first, second+1)
    {
        if (fas.find(i) == fas.end())
        {
            int j = sqrt(i);
            if ((sqrt(i)-j == 0.0) && ispalindrome(i) && ispalindrome(j)) fas[i] = true;
            else fas[i] = false;
        }

        if (fas[i]) total++;
    }
    printf(" %d\n", total);
}

int main()
{
    int nc;
    int count = 0;
    scanf("%d ", &nc);
    while (nc-- > 0)
    {
        printf("Case #%d:", ++count);
        getInput();
        process();

        /*CLEAR GLOBAL VARIABLES!*/

        /*CLEAR GLOBAL VARIABLES!*/
    }

    return 0;
}
