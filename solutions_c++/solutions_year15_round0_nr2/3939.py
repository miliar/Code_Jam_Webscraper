#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
int a,b,c,d,t;
vector<int> in;
map<vector<int>,int> dp;
int query(vector<int> curr)
{
    if (*max_element(curr.begin(),curr.end())==1)return 1;
    if (dp.find(curr)!=dp.end())return dp[curr];
    int ans=*max_element(curr.begin(),curr.end());
    vector<int> k;
    for (int i=0;i<curr.size();i++)
    {
        for (int j=1;j<curr[i];j++)
        {
            k=curr;
            k[i]-=j;
            k.push_back(j);
            sort(k.begin(),k.end());
            ans=min(ans,1+query(k));
        }
    }
    dp[curr]=ans;
    return ans;
}
int main()
{
    freopen("lw.in","r",stdin);
    freopen("C:/Users/Penguin/Desktop/OUT.txt","w",stdout);
    scanf("%i",&t);
    for (int ii=1;ii<=t;ii++)
    {
        printf("Case #%i: ",ii);
        scanf("%i",&a);
        in.clear();
        dp.clear();
        for (int i=0;i<a;i++)
        {
            scanf("%i",&b);
            in.push_back(b);
        }
        printf("%i\n",query(in));
    }
    return 0;
}
