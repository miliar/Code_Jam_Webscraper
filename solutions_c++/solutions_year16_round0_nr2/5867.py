#include <cstdio>
#include <string>
#include <map>
#include <queue>
#include <cassert>
#include <algorithm>
#include <cstring>

using namespace std;

const int MAXN = 105;
char buff[MAXN];

map <string, int> M;

int bf () {
  int n = strlen(buff);
  int ans = 0;
  while (n > 0) {
    if (buff[n-1] == '+') --n;
    else {
      int pos = 0;
      while (buff[pos] == '+') ++pos;
      if (pos) {
	for (int i = 0; i < pos; ++i) buff[i] = '-';
	++ans;
      } else {
	++ans;
	reverse(buff, buff + n);
	for (int i = 0; i < n; ++i) 
	  if (buff[i] == '+') buff[i] = '-';
	  else buff[i] = '+';
      }
    }
  }
  return ans;
}

void solve (){
  scanf("%s", buff);
  string s = buff;
  printf("%d\n", bf());
}

void init () {
  string s = "";
  queue <string> Q;
  for (int i = 1; i <= 10; ++i) {
    s += "+";
    Q.push(s);
    M[s] = 0;
  }

  while (!Q.empty()) {
    string curr = Q.front();
    for (int i = 1; i <= (int)curr.size(); ++i) {
      string tmp = curr;
      reverse(tmp.begin(), tmp.begin() + i);
      for (int j = 0; j < i; ++j)
	if (tmp[j] == '+') tmp[j] = '-';
	else tmp[j] = '+';
      
      if (M.count(tmp)) continue;
      M[tmp] = M[curr] + 1;
      Q.push(tmp);
    }
    Q.pop();
  }
}

int main (void){
  int tc; scanf ("%d", &tc);
  init();
  for (int i = 1; i <= tc; ++i){
    printf("Case #%d: ", i);
    solve();
  }

  return 0;
}


