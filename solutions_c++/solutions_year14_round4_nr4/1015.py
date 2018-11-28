#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <queue>
#include <fstream>
#include <cstring>

using namespace std;
typedef long long LL;

int n, m, ret, cnt;
string s[10];
int a[10];

void go(int cur)
{
    if (cur>=n)
    {
        set<string> ss;
        int t=0;
        for (int k=0;k<m;k++)
        {
            ss.clear();
            int got=0;
            for (int i=0;i<n;i++)
                if (a[i]==k)
                {
                    got=1;
                    string curs="";
                    for (int j=0;j<=s[i].size();j++)
                    {
                        ss.insert(curs);
                        if (j==s[i].size()) break;
                        curs+=s[i][j];
                    }
                }
            if (!got) return;
            t+=ss.size();
        }
            if (ret==t) cnt++;
            else if (ret<t)
            {
                ret=t;
                cnt=1;
            }
        return;
    }
    for (int i=0;i<m;i++)
    {
        a[cur]=i;
        go(cur+1);
    }
}
int main()
{
    freopen("trie_shading.in","r",stdin);
    freopen("trie_shading.out","w",stdout);
    int tc, nt=1;
    cin>>tc;
    while (tc--)
    {
        cin>>n>>m;
        for (int i=0;i<n;i++) cin>>s[i];
        ret=0;
        cnt=0;
        go(0);
        cout<<"Case #"<<nt++<<": "<<ret<<" "<<cnt<<endl;
    }
}
