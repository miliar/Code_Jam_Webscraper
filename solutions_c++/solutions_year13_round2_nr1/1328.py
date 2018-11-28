#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <limits>
#include <cctype>

using namespace std;

vector<int>v;
int n;

map<pair<int,int>,int>m;
int solve(int ind,int A)
{

    if(ind==n)
        return 0;
        pair<int,int> p=make_pair(ind,A);
        if(m.count(p))
            return m[p];
//cout<<A<<" "<<v[ind]<<endl;
        int ret=0,a=1<<30,b=1<<30;

        if(A>v[ind])
            ret=solve(ind+1,A+v[ind]);
        else
        {
            if(A>1)
                 a=1+solve(ind,A+A-1);
             b=1+solve(ind+1,A);
            ret=min(a,b);
        }
        return m[p]=ret;
}
int main()
{
freopen("2.txt","r",stdin);
freopen("3.txt","w",stdout);
int tc;
scanf("%d",&tc);

for(int ic=1;ic<=tc;ic++)
{
    v.clear();
    m.clear();
    int A=0;
    int ret=0,a;
    scanf("%d%d",&A,&n);
    for(int i=0;i<n;i++)
    {
        scanf("%d",&a);
        v.push_back(a);
        //cout<<a<<" ";
    }
    sort(v.begin(),v.end());

    printf("Case #%d: %d\n",ic,solve(0,A));

}


}

