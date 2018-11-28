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

int cmp( const void *a , const void *b)
{
    return *(double *)a > *(double *)b ? 1 : -1;
}

int main()
{
    int t, n, tn, i, j;
    int maxn, minn;
    double a[1002], b[1002];
    freopen("C:\\Users\\ZLi\\CodeBlockCode\\Test\\GCJ2014PreC\\bin\\Debug\\D-large.in", "r", stdin);
	freopen("C:\\Users\\ZLi\\CodeBlockCode\\Test\\GCJ2014PreC\\bin\\Debug\\output.txt", "w", stdout);

	cin>>t;
	for(tn = 1; tn <= t; tn++)
    {
        cin>>n;
        for(i = 0; i < n; i++)
            cin>>a[i];
        for(i = 0; i < n; i++)
            cin>>b[i];

        qsort(a,n,sizeof(a[0]),cmp);
        qsort(b,n,sizeof(a[0]),cmp);
        /*for(i = 0; i < n; i++)
            cout<<a[i]<<" ";
        cout<<endl;
        for(i = 0; i < n; i++)
            cout<<b[i]<<" ";
        cout<<endl;*/

        maxn = minn = 0;
        i = 0;
        for(j = 0; j < n;)
        {
            if(a[i] > b[j])
            {
                maxn++;
                j++;
            }
            i++;
            if(i == n)
                break;
        }

        j = 0;
        for(i = 0; i < n;)
        {
            if(b[j] > a[i])
            {
                minn++;
                i++;
            }
            j++;
            if(j == n)
                break;
        }

        cout<<"Case #"<<tn<<": "<<maxn<<" "<<n-minn<<endl;
    }

    return 0;
}
