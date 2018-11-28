
#include<cstdio>
#include<iostream>
#include<vector>
#include<map>
#include<stack>
#include<cstdio>
#include<iostream>
#include<vector>
#include<map>
#include<stack>
#include<queue>
#include<bitset>
#include<list>
#include<iomanip>
#include<string>
#include<climits>
#include <sstream>
#include <fstream>
#include<cctype>
#include<ctime>
#include<cassert>
#include <numeric>
#include <functional>
#include<cstring>
#include<cmath>
#include<iterator>
#include <memory.h>
#include<utility>
#include <ctime>
#include<deque>
#include<algorithm>
#define min3(a,b,c) min(a,min(b,c))
#define max3(a,b,c) max(a,max(b,c))
#define min4(a,b,c,d) min(min(a,b),min(c,d))
#define max4(a,b,c,d) max(max(a,b),max(c,d))
#define maxall(envy) *max_element(v.begin(),v.end())
#define minall(envy) *min_element(v.begin(),v.end())
#define pb push_back
#define mk make_pair
#define SORT(envy) sort(v.begin(),v.end())
#define UN(envy) SORT(envy), (v).earse(unique(v.begin(),v.end()),v.end())
#define FILL(a,d) memset(a,d,sizeof(angel))
#define LL long long
#define PI 2*acos(0.0)
#define pi pair<int,int>
using namespace std;
const int inf=1000000007;

int main()
{
    LL i,j,k,l,m,n;
    int nc,tc=0;
    freopen("input.in","r",stdin);
    freopen("output.in","w",stdout);
    cin>>nc;
    while(nc--)
    {
        cin>>n>>m;
        int count=0;
        for(i=n;i<=m;i++)
        {
            if(i==1)
                count++;
            if(i==4)
                count++;
            if(i==9)
                count++;
            if(i==121)
                count++;
            if(i==484)
                count++;
        }
        cout<<"Case #"<<++tc<<": "<<count<<endl;
    }

    return 0;
}
