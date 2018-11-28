#include<bits/stdc++.h>
using namespace std;

int p[30];
string s;
vector<int>ans;
int flag3 = 0;
string num[12]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
void init()
{
    memset(p,0,sizeof(p));
    ans.clear();
    flag3=0;
}
void dfs(int x)
{
    if(x==10)return;
    if(flag3)return;
    int flag2 = 0;
    for(int i=0;i<26;i++)
        if(p[i]>0)flag2=1;
    if(flag2==0)
    {
        flag3 = 1;
        return;
    }
    for(int i=0;i<num[x].size();i++)
        p[num[x][i]-'A']--;
    int flag = 0;
    for(int i=0;i<num[x].size();i++)
        if(p[num[x][i]-'A']<0)
            flag = 1;
    if(flag==0)
    {
        ans.push_back(x);
        dfs(x);
        if(flag3)return;
        ans.pop_back();
    }
    for(int i=0;i<num[x].size();i++)
        p[num[x][i]-'A']++;
    dfs(x+1);
    if(flag3)return;
}
void solve(int x)
{
    init();
    cin>>s;
    for(int i=0;i<s.size();i++)
        p[s[i]-'A']++;
    dfs(0);
    printf("Case #%d: ",x);
    for(int i=0;i<ans.size();i++)cout<<ans[i];
    cout<<endl;
}
int main()
{
    freopen("123123.in","r",stdin);
    freopen("123123.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)solve(i);
    return 0;
}
