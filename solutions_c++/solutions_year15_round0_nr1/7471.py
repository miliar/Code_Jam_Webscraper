#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <limits>
#include<stack>
#include<queue>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <sstream>
#define loop(x,y) for(int i=x;i<y;i++)
#define inp(x) cin>>x
#define out(x) cout<<x<<endl
#define MAX 1007
using namespace std;
int main()
{
    freopen("A-large.in","rt",stdin);
    freopen("A-large.out","wt",stdout);

    int test;
    inp(test);
    for(int t = 0; t < test; t++)
    {
        int n;
        inp(n);
        long aud = 0, count = 0;
        char s[MAX];
        inp(s);
        if(s[0] == '0')
        {
            count++;
            aud++;
        }
        loop(1,n+1)
        {
            int x = s[i-1] - 48;
            aud += x;
            if(i > aud && s[i] != '0')
            {
                int y = i - aud;
                count = count + y;
                aud = aud + y;
            }
        }
        cout<<"Case #"<<t+1<<": "<<count<<endl;
    }
    return 0;
}
