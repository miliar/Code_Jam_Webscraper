#include<cstdio>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;
int n,r,p,s;
string mem[25][300];
string solve(char t, int level)
{
  if(level==0) {
    string s="";
    s.push_back(t);
    return s;
  }
  if (mem[level][t-'A']!="")return mem[level][t-'A'];
  if (t=='P')
    return mem[level][t-'A'] = min(solve('P',level-1) + solve('R',level-1), 
			       solve('R',level-1) + solve('P',level-1));
  else if (t=='R')
    return mem[level][t-'A'] = min(solve('R',level-1) + solve('S',level-1),
			      solve('S',level-1) + solve('R',level-1));
  else if (t=='S')
    return mem[level][t-'A'] = min(solve('P',level-1) + solve('S',level-1),
			       solve('S',level-1) + solve('P',level-1));
  throw "perdi";
}
bool bate(string ss){
  int a=0,b=0,c=0;
  for(int i=0;i<(int)ss.size();i++){
    if(ss[i]=='R')a++;
    else if(ss[i]=='P')b++;
    else if(ss[i]=='S')c++;
  }
  return a==r && b==p && c==s;
}
int main (){
  int tt;
  scanf("%d",&tt);
  for(int rr=1;rr<=tt;rr++){
    scanf("%d %d %d %d",&n,&r,&p,&s);
    bool ok = false;
    string ss="zzzz";
    string ret="ZZZZ";
    ss = solve('R',n);
    if (bate(ss)){ok=true;ret=min(ret,ss);}

    ss = solve('P',n);
    if (bate(ss)){ok=true;ret=min(ret,ss);}

    ss = solve('S',n);
    if (bate(ss)){ok=true;ret=min(ret,ss);}

    if (ok)
      printf("Case #%d: %s\n",rr,ret.c_str());
    else
      printf("Case #%d: IMPOSSIBLE\n",rr);
  }

  return 0;
}
