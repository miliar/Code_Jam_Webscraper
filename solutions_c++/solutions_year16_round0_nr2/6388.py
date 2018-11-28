#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

#include <vector>
#include <queue>
#include <stack>
#include <array>
#include <map>
#include <set>
#include <iterator>
#include <algorithm>
#include <numeric>
#include <functional>

using namespace std;

#define UL 100

int solve(const string & s) {
    int l = s.length();
    int nc = 0;
    char pv = s[0];
    for(int i = 1; i < l; ++i)
    {
        if (s[i]!=pv) ++nc;
        pv = s[i];
    }
    if (s[l-1] == '-') ++nc;
    return nc;
}


int main(int argc, char * argv[])
{
    int t;
    scanf("%d",&t);
    while(t--) {
        char s[UL];
        scanf("%s",s);
        static int id = 0;
        printf("Case #%d: %d\n",++id, solve(s));
    }
    return 0;
}
