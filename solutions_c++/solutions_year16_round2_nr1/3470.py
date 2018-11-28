//In the Name of God

#include <bits/stdc++.h>
using namespace std;
typedef long long lol;
string dig[10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
vector <char> v;
string s;
int cnt[60],now;

bool has(int ind)
{
  for(int i=0;i<dig[ind].size();i++)
    if(cnt[dig[ind][i]-'A']==0)
      return false;
  return true;
}

void take(int ind,int c)
{
  for(int i=0;i<dig[ind].size();i++)
    cnt[dig[ind][i]-'A']+=c;
}

void bt(int x,int len=0)
{
  if(len>s.length())
    return;
  for(int i=x;i<10;i++)
    if(has(i))
      {
	v.push_back(i+'0');
	take(i,-1);
	bt(i,len+dig[i].size());
	take(i,+1);
	v.pop_back();
      }
  if(len==s.length())
    {
      cout<<"Case #"<<now+1<<": ";
      for(int i=0;i<v.size();i++)
	cout<<v[i];
      cout<<endl;
      return;
    }
}

int main()
{
  ios::sync_with_stdio(false);
  int t;
  cin>>t;
  for(int ttt=0;ttt<t;ttt++)
    {
      now=ttt;
      cin>>s;
      memset(cnt,0,sizeof cnt);
      for(int i=0;i<s.length();i++)
	cnt[s[i]-'A']++;
      bt(0);
    }
  return 0;
}
