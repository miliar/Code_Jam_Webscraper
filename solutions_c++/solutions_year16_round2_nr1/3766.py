#include <bits/stdc++.h>

using namespace std;

map<char, string> hs;
char seq[2001], ans[2001];
int l, lans;

bool verify(char n, int used)
{
  if(used == l) return true;
  if(n > '9') return false;
  string temp = hs[n];
  int cnt = 0;
  bool found;
  for(int i = 0; i < temp.size(); ++i)
  {
    found = false;
    for(int j = 0; j < l && !found; ++j)
      if(seq[j] == temp[i])
      {
        seq[j] = '*';
        ++cnt;
        found = true;
      }
    if(!found)
      break;
  }
  bool anss = false;
  if(cnt == temp.size())
  {
    anss = verify(n, used + cnt);
    if(anss)
      ans[lans++] = n;
  }
  for(int i = 0, j = 0; i < l && j < cnt; ++i)
    if(seq[i] == '*')
      seq[i] = temp[j++];
  if(cnt < temp.size() || !anss)
    anss = verify(n + 1, used);
  return anss;
}

void init()
{
  hs['0'] = "ZERO";
  hs['1'] = "ONE";
  hs['2'] = "TWO";
  hs['3'] = "THREE";
  hs['4'] = "FOUR";
  hs['5'] = "FIVE";
  hs['6'] = "SIX";
  hs['7'] = "SEVEN";
  hs['8'] = "EIGHT";
  hs['9'] = "NINE";
}

int main()
{
  int t, cas = 0;
  scanf("%d", &t);
  init();
  while(t--)
  {
    scanf("%s", &seq);
    l = strlen(seq);
    lans = 0;
    memset(ans, 0, sizeof ans);
    verify('0', 0);
    sort(ans, ans + lans);
    printf("Case #%d: %s\n", ++cas, ans);
  }
  return 0;
}
