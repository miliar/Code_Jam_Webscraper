#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

map<string,int>Mymap;

string make_str(vector<int> ar)
{   sort(ar.begin(),ar.end());
    string rt="";
    int i,lim=ar.size();
    for(i=0;i<lim;i++)
        rt=rt+(char)(ar[i]+'0');
    return rt;
}

int getans(vector<int>&ar)
{   string s1=make_str(ar);
    if(Mymap[s1])
        return Mymap[s1];
    int i,id=0,mx=ar[0],lim=ar.size();
    for(i=0;i<lim;i++)
        {
            if(mx<ar[i])
            {
                mx=ar[i];id=i;
            }
        }
    if(mx<4)
        {Mymap[s1]=mx;
            return mx;}
    vector<int>ar2;
    for(i=0;i<lim;i++)
        if(ar[i]>1)
        ar2.push_back(ar[i]-1);
    int ans=1+getans(ar2);
    int tp,j,k;
    i=id;
    {
        if(ar[i]>1)
        {
            for(j=1;j<ar[i]/2+1;j++)
            {
                ar2=ar;
                ar2[i]-=j;
                ar2.push_back(j);
                tp=1+getans(ar2);
                ans=min(ans,tp);
            }
        }
    }
    Mymap[s1]=ans;
    return ans;
}
int main()
{   freopen("B-small-attempt1.in", "r", stdin);
    freopen("result1.txt", "w", stdout);
    int i,j,T,D,a;
    scanf("%d",&T);
    for(i=1;i<T+1;i++)
    {
    scanf("%d",&D);
    vector<int>MyV;
    for(j=0;j<D;j++)
    {
    scanf("%d",&a);
    MyV.push_back(a);
    }

    printf("Case #%d: %d\n",i,getans(MyV));
    }
}
