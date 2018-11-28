#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
    int t;
    double c, f, x, s;
    int tn;
    double cur, next, temp;
    freopen("C:\\Users\\ZLi\\CodeBlockCode\\Test\\GCJ2014PreB\\bin\\Debug\\B-large.in", "r", stdin);
	freopen("C:\\Users\\ZLi\\CodeBlockCode\\Test\\GCJ2014PreB\\bin\\Debug\\output.txt", "w", stdout);

    cin>>t;
    for(tn = 1; tn <= t; tn++)
    {
        s = 2.0;
        cin>>c>>f>>x;

        cur = x/s;
        temp = 0.0;
        while(1)
        {
            temp += c/s;
            s+=f;
            next = temp+x/s;

            if( cur<next )
                break;
            else
            {
                cur = next;
            }
        }
        printf("Case #%d: %.7lf\n", tn, cur);
        //cout<<"Case #"<<tn<<": "<<cur<<endl;
    }

    return 0;
}
