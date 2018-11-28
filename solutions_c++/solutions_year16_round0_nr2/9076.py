#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
#include<vector>
#include<string>
using namespace std;

int cnt;

string reverse_junjo(string s, int pos)
{
  for(int i = 0; i <= pos / 2; i++){
    string tmp;
    tmp = s.substr(i, 1);
    s = s.replace(i, 1, s.substr(pos - i, 1));
    s = s.replace(pos - i, 1, tmp);
  }
  return s;
}

string reverse_string(string s, int pos)
{
  for(int i = 0; i <= pos; i++){
    if(s.substr(i, 1) == "-"){
      s = s.replace(i, 1, "+");
      continue;
    }
    if(s.substr(i, 1) == "+"){
      s = s.replace(i, 1, "-");
      continue;
    }
  }
  return s;
}

string reverse(string s, int pos)
{
  s = reverse_junjo(s, pos);
  s = reverse_string(s, pos);
  cnt++;
  return s;
}

string convert_head_to_blank(string s)
{
  if(s.substr(0, 1) == "-"){
    return s;
  }
  cnt++;
  for (int i = 0; i < (int)s.size(); i++){
    if(s.substr(i, 1) == "-") return s;

    if(s.substr(i, 1) == "+"){
      s = s.replace(i, 1, "-");
    }
  }
  return s;
}

int make_pancake(string s)
{
  cnt = 0;

  for(int i = (int)s.size() - 1; i >= 0; i--){
    if(s.substr(i, 1) == "-"){
      s = convert_head_to_blank(s);
      s = reverse(s, i);
    }
  }
  return cnt;
}


int main()
{
  string pancake_stack;
  int N;

  cin >> N;
  for(int i = 0; i < N; i++){
    cin >> pancake_stack;
    int result = make_pancake(pancake_stack);
    printf("Case #%d: %d\n", i + 1, result);
  }
  return 0;
}