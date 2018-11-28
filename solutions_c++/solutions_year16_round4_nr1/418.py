#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<vector>
#include<iostream>
#include<string>
#include<string.h>
using namespace std;
int len;
int cnt[3];
string s[3]= {"P","S","R"};
string solve(int low,int high,int cur)
{
    if(low==high)
    {
        cnt[cur]++;
        string r="";
        return r+s[cur];
    }
    int mid=low+high>>1;
    string left=solve(low,mid,cur);//win
    string right=solve(mid+1,high,(cur+2)%3);//lose
    if(left>right)
        swap(left,right);
    return left+right;
}
int main()
{
    freopen("A-large (3).in","r",stdin);
    freopen("a2.out","w",stdout);
    int t,ca=0;
    scanf("%d",&t);
    while(t--)
    {
        vector<string>ans;
        int p,r,s,n;
        scanf("%d%d%d%d",&n,&r,&p,&s);
        for(int i=0; i<3; ++i)
        {
            memset(cnt,0,sizeof(cnt));
            string temp=solve(1,1<<n,i);
            if(cnt[0]==p&&cnt[1]==s&&cnt[2]==r)
                ans.push_back(temp);
        }
        if(ans.size()==0)
            printf("Case #%d: IMPOSSIBLE\n",++ca);
        else
        {
            sort(ans.begin(),ans.end());
            printf("Case #%d: %s\n",++ca,ans[0].c_str());
        }
    }
}
