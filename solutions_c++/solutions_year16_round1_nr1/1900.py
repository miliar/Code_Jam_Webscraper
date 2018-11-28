#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int main () {
  int T;
  scanf("%d", &T);
  for(int caso = 1; caso <= T; caso++) {
    char str[1010];
    scanf(" %s", str);
    
    deque<char> dq;
    dq.push_front(str[0]);
    int n = strlen(str);
    for(int i = 1; i < n; i++) {
      if(str[i] >= dq.front()) dq.push_front(str[i]);
      else dq.push_back(str[i]);
    }
    printf("Case #%d: ",caso);
    for(auto it = dq.begin(); it != dq.end(); it++)
      printf("%c", *it);
    printf("\n");
  }
  return 0;    
}
