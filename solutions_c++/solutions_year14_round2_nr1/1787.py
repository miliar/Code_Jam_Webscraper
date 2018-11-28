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
int ans;

string make_equal(string a,string b)
{
    if(a[0]!=b[0])
    {ans=-10000000;
        return a;}
    string ret="";
    int i=0,j=0;
    while(i<a.length() && j<b.length())
    {
        if(a[i]==b[j])
        {  ret=ret+a[i];
            i++;j++;
        }
        else if(a[i]!=b[j])
        {
            if(a[i]==a[i-1])
            {i++;ans++;}
            else if(b[j]==b[j-1])
            {
                j++;ans++;
            }
            else
            {
                ans=-10000000;return a;
            }
        }
    }
    if(i<a.size())
    {
        while(i<a.size())
        {
            if(a[i]!=a[i-1])
            {
                ans=-1000000;return a;
            }
            i++;ans++;
        }
    }
    if(j<b.size())
    {
        while(j<b.size())
        {
            if(b[j]!=b[j-1])
            {
                ans=-10000000;return a;
            }
            j++;ans++;
        }
    }
    return ret;
}
int main()
{   freopen("A-small-attempt0.in", "r", stdin);
    freopen("result.txt", "w", stdout);
    int T;
    scanf("%d",&T);
    int i,j,k;
    for(i=1;i<T+1;i++)
    {
        ans=0;
       vector<string>Mv;
       int N;
       string st;
       scanf("%d",&N);
       for(j=0;j<N;j++)
       {
           cin>>st;
           Mv.push_back(st);
       }
       st=Mv[0];
       for(j=1;j<N;j++)
       {
           st=make_equal(st,Mv[j]);
           if(ans<0)
            break;
       }
       if(ans<0)
        printf("Case #%d: Fegla Won\n",i);
       else
        printf("Case #%d: %d\n",i,ans);
    }
}
