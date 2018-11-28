#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> vec;

string func()
{
  for(int i = 0; i < 4; ++i)
    for(int j = 0; j < 4; ++j)
      if(vec[i][j] == '.') return "Game has not completed";

  return "Draw";
}

bool check(char ch)
{
  bool f, t;
  for(int i = 0; i < 4; ++i){
    f = t = true;
    for(int j = 0; j < 4 && f; ++j){
      if(ch == vec[i][j]) continue;
      else if(vec[i][j] == 'T' && t) t = false;
      else f = false; 
    }
    if(f) return true;

    f = t = true;
    for(int j = 0; j < 4 && f; ++j){
      if(ch == vec[j][i]) continue;
      else if(vec[j][i] == 'T' && t) t = false;
      else f = false; 
    }
    if(f) return true;
  }

  t = f = true;
  for(int i = 0; i < 4; ++i){
    if(ch == vec[i][i]) continue;
    else if(vec[i][i] == 'T' && t) t = false;
    else f = false;
  }
  if(f) return true;

  t = f = true;
  for(int i = 0; i < 4; ++i){
    if(ch == vec[3-i][i]) continue;
    else if(vec[3-i][i] == 'T' && t) t = false;
    else f = false;
  }
  if(f) return true;

  t = f = true;
  for(int i = 0; i < 4; ++i){
    if(ch == vec[i][3-i]) continue;
    else if(vec[i][3-i] == 'T' && t) t = false;
    else f = false;
  }

  return f;
}

int main()
{
  int N;
  string str;
  cin >> N;
  vec = vector<string>(4);

  for(int cs = 1; cs <= N; ++cs){
    for(int i = 0; i < 4; ++i)
      cin >> vec[i];
    cout << "Case #" << cs << ": ";

    if(check('O')){
      str = "O won";
    } else if(check('X')){
      str = "X won";
    } else {
      str = func();
    }

    cout << str << endl;
  }

  return 0;
}
