#include <vector>
#include <iterator>
#include <list>
#include <map>
#include <math.h>
#include <cmath>
#include <set>
#include <queue>
#include <deque>
#include <string>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <string.h>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstdlib>
#include <ctime>

using namespace std;

map<int,set<vector<int> > >mop;
string arr[10];
int N,m;
vector<int>v;
void bt(int i)
{
    if(i==N)
    {
        set<string>s[6];
        for(int f=0;f<i;f++)
        {
            string t;
            for(int f1=0;f1<arr[f].size();f1++)
            {
                s[v[f]].insert("");
                t+=arr[f][f1];
                s[v[f]].insert(t);
            }
        }
        int temp=0;
        for(int f=0;f<m;f++)
            temp+=s[f].size();
        mop[-temp].insert(v);
        return;
    }
    for(int f=0;f<m;f++)
    {
        v.push_back(f);
        bt(i+1);
        v.pop_back();
    }
}

int main()
{
    freopen ("input.txt","r",stdin);
    freopen ("output.txt","w",stdout);
    int t,n;
    cin>>t;
    for(int F=1;F<=t;F++)
    {
        mop.clear();
        cin>>N>>m;
        for(int f=0;f<N;f++)
            cin>>arr[f];
        bt(0);
        v.clear();
        cout<<"Case #"<<F<<": "<<-mop.begin()->first<<" "<<mop.begin()->second.size()<<endl;
    }
}
