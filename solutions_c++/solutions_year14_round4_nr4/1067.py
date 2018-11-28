#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
#include <iostream>
using namespace std;

vector<int> s[4];
string a[20];
int m,n;
int cnt[10000];
int com(int i)
{
    if(s[i].size()==0) return 0;
    vector<string> ss;
    for(int k=0;k<s[i].size();k++)
    {
        string t="";
        string str=a[s[i][k]];
        for(int j=0;j<str.size();j++)
        {
            t+=str[j];
            ss.push_back(t);
        }
    }
    sort(ss.begin(),ss.end());
    string ans=ss[0];
    int cnt=1;
    for(int j=1;j<ss.size();j++) if(ss[j]!=ans)
    {
        ans=ss[j];
        cnt++;
    }
    return cnt+1;
}
void dfs(int step)
{
//cout<<step<<" "<<m<<endl;
    if(step==m)
    {

        int tmp=0;
        for(int i=0;i<n;i++)
        {
            if(s[i].size()==0) return ;
       //     cout<<i<<" "<<s[i].size()<<endl;
            tmp+=com(i);
        }
        cnt[tmp]++;
        return ;
    }
    for(int i=0;i<n;i++)
    {
        s[i].push_back(step);
        dfs(step+1);
        s[i].pop_back();
    }
}
int main()
{
    freopen("D.in","r",stdin);
    freopen("D.out","w",stdout);
    int t;
    cin>>t;
    int cs=0;
    while(t--)
    {
      cin>>m>>n;
      for(int i=0;i<m;i++) cin>>a[i];
      memset(cnt,0,sizeof(cnt));
      for(int i=0;i<n;i++) s[i].resize(0);
      dfs(0);
    //  cout<<"yes\n";
      int maxans=0;
      for(int i=1;i<10000;i++) if(cnt[i]) maxans=i;
      cout<<"Case #"<<++cs<<": "<<maxans<<" "<<cnt[maxans]<<endl;

    }
    return 0;
}
