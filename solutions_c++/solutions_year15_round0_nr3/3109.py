#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <map>
#include <string>

int sign(int a){
  return a >= 0 ? 1 : -1;
}

int abs(int a){
  return a > 0 ? a : -a;
}

char mult(char lhs, char rhs){
  std::map<char, std::map<char, char> > d;
  d[1][1] = 1;
  d[1]['i'] = 'i';
  d[1]['j'] = 'j';
  d[1]['k'] = 'k';

  d['i'][1] = 'i';
  d['i']['i'] = -1;
  d['i']['j'] = 'k';
  d['i']['k'] = -'j';

  d['j'][1] = 'j';
  d['j']['i'] = -'k';
  d['j']['j'] = -1;
  d['j']['k'] = 'i';

  d['k'][1] = 'k';
  d['k']['i'] = 'j';
  d['k']['j'] = -'i';
  d['k']['k'] = -1;

  return sign(lhs) * sign(rhs) * d[abs(lhs)][abs(rhs)];
}

bool ans(int L, int X, char *s){
  std::string str;
  for(int i = 0;i < X % 4;++i){
    str += s;
  }
  X -= X % 4;
  char search_for[] = {'i', 'j', 'k', 1};
  int n_search_for = 4;
  for(int i = 0, j = 0;i < 4;++i){
    char current = 1;
    bool expended = false;
    for(;;++j){
      if(current == search_for[i] && (i != n_search_for - 1 || j == str.length())){
        break;
      }
      if(j == str.length()){
        if(expended || X == 0){
          return false;
        }else{
          for(int i = 0;i < 4;++i){
            str += s;
          }
          X -= 4;
          expended = true;
        }
      }
      current = mult(current, str[j]);
    }
  }
  return true;
}

int main(){
  int T;
  scanf("%d", &T);
  for(int i = 1;i <= T;++i){
    int L, X;
    scanf("%d%d", &L, &X);
    char *s = new char[L];
    scanf("%s", s);
    printf("Case #%d: %s\n", i, ans(L, X, s) ? "YES": "NO");
    delete[] s;
  }
}
