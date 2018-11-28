//ShivamRana...
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <list>
#include <deque>
#include <stack>
#include <iterator>
#include <string>
#include <sstream>
#include <iostream>
#include <fstream>
#include <functional>
#include <numeric>
#include <algorithm>
using namespace std;
#define ll long long
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int t;
    cin>>t;
    for(int cs=1;cs<=t;cs++)
    {
        printf("Case #%d: ",cs);
        int a,b,k;
        cin>>a>>b>>k;
        ll ans=0;
        for(int i=0;i<a;i++)
        {
        	for(int j=0;j<b;j++)
        	{
        		int x=i&j;
        		if(x<k)
        			ans++;
        	}
        }
        cout<<ans<<endl;
    }
    return 0;
}
