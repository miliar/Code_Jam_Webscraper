#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <iostream>

using namespace std;

const int MAXN = 10;
string s[MAXN];
pair<string,int> sp[MAXN];
int lcp[MAXN][MAXN];

int get_lcp(string a,string b)
{
  int r = 0;
  for(; r < a.length() && r < b.length() && a[r] == b[r]; r++) ;
  return r;
}

struct miu
{
  int lst[MAXN],cnt;
  miu() : cnt(0) {}
  int push_back(int v)
  {
    lst[cnt++] = v;
    return s[v].length() - (cnt == 1 ? 0 : lcp[lst[cnt-1]][lst[cnt-2]]);
  }
  void pop_back()
  {
    --cnt;
  }
} seq[MAXN];

pair<int,int> g_ans;
void search(int m,int n,int k,int ans)
{
  if (k < m)
    {
      int p = sp[k].second;
      for(int i = 0; i < n; i++)
	{
	  search(m,n,k + 1,ans + seq[i].push_back(p) );
	  seq[i].pop_back();
	}
    }
  else
    {
      for(int i = 0; i < n; i++)
	if (seq[i].cnt == 0) return ;
      if (ans > g_ans.first)
	{
	  g_ans = make_pair(ans,1);
	}
      else if (ans == g_ans.first) g_ans.second++;
    }
}

int main()
{
  int t;
  scanf("%d",&t);
  for(int case_num = 1; case_num <= t; case_num++)
    {
      printf("Case #%d: ",case_num);

      int m,n;
      cin >> m >> n;

      for(int i = 0; i < m; i++)
	{
	  cin >> s[i];
	  sp[i] = make_pair(s[i],i);
	}
      sort(sp,sp + m);

      for(int i = 0; i < m; i++)
	for(int j = 0; j < m; j++)
	  {
	    lcp[i][j] = get_lcp(s[i],s[j]);
	  }

      g_ans = make_pair(-1,-1);
      search(m,n,0,n);

      printf("%d %d\n",g_ans.first,g_ans.second);
    }
  return 0;
}
