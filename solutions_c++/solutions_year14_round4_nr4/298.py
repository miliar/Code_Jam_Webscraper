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
#include <cstring>
#include <queue>
using namespace std;
#define rep(i,n) for(int i=0;i<n;i++)
#define pb push_back
#define mp make_pair
#define F first
#define S second
string str;
vector <string> st;
int maxn;
int num;
void dfs(vector <string> s,int n,int sum)
{
    if((n==0) && (s.size() == 0))
    {
        if(sum>maxn)
        {
            num = 1;
            maxn = sum;
        }
        else if(sum == maxn)
            num++;
    }
    if(n==0)return ;
    int nu = s.size();
    int st = 1,en = (1<<nu)-1;
    if(n == 1)
    {
        st = (1<<nu)-1;
        en = (1<<nu);
    }
    for(int i=st;i<en;i++)
    {
        set <string> st;
        vector <string> le;
        le.clear();
        st.insert("");

        for(int j=0;j<nu;j++)
            if(i&(1<<j))
            {
                 string sss = "";
                 for(int k=0;k<s[j].size();k++)
                 {
                     sss+=s[j][k];
                     st.insert(sss);
                 }
            }
            else
            {
                le.push_back(s[j]);
            }
        //cout << n << " " << st.size() << endl;
        dfs(le,n-1,sum+st.size());
    }
}
int main()
{
    //D-small-attempt0.in
    freopen("D-small-attempt0.in", "r", stdin);
    freopen("D-small1.out", "w", stdout);
    int T;
    cin>>T;
    rep(cas,T)
    {
        int n,m;
        st.clear();
        cin>>n>>m;
        rep(i,n){
            cin>>str;
            st.push_back(str);
        }

        maxn = 0;
        num = 0;
        //for(int i=0;i<st.size();i++)
        //cout << st[i] << endl;
        dfs(st,m,0);
        printf("Case #%d: %d %d\n",cas+1,maxn,num);
    }
}







