#include<iostream>
#include<cstdio>
#include<vector>
#include<string>
#include<map>
#include<set>
using namespace std;

string produce(char x, int level){
  if(level== 0){
    
    return string(1, x);
  }
  if (x=='R')
    return produce('R', level -1) + produce('S', level-1);
  if (x=='S')
    return produce('S', level -1) + produce('P', level -1);
  if(x=='P')
    return produce('P', level -1) + produce('R', level -1);
}
string minimal(string s){
  if (s.size() == 1)
    return s;
  int n = s.size();
  string a = minimal(s.substr(0, n/2));
  string b = minimal(s.substr(n/2,n/2));
  if (a < b){
    return a+b;
  }
  return b+a;
}
bool count(string s, int R, int S, int P){
  for(int i = 0; i < s.size();i++){
    if(s[i] =='R')
      R--;
    if(s[i]=='S')
      S--;
    if(s[i] =='P')
      P--;
  }
  return (R==0)&&(S==0) &&(P==0);
}
void work()
{
  int N, R, S, P;
  scanf("%d%d%d%d",&N,&R, &P, &S);
  string s = produce('R', N);
  string res ="Z";
  if (count(s, R, S, P)){
    res = min(res, minimal(s));
  }
  s = produce('S', N);
  if(count(s, R, S, P)){
    res = min(res, minimal(s));
  }
  s = produce('P', N);
  if(count(s, R,S,P)){
    res = min(res, minimal(s));
  }
  if(res[0] == 'Z')
    cout << "IMPOSSIBLE" << endl;
  else
    cout << res << endl;
}
int main()
{
  int T;
  scanf("%d",&T);
  for(int i =1; i <=T; i++){
    printf("Case #%d: ", i);
    work();
  }
}
