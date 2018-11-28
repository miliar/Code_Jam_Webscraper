#include <bits/stdc++.h>
using namespace std;
int main(){
  int T;
  scanf("%d",&T);
  for(int c = 1; c <= T; c++){
    string str;
    cin >> str;
    deque<char> dq;
    for(int i = 0; i < str.size(); i++){
      if(dq.empty()) dq.push_back(str[i]);
      else {
        if(str[i] >= dq.front()) dq.push_front(str[i]);
        else dq.push_back(str[i]);
      }
    }
    printf("Case #%d: ",c);
    while(!dq.empty()){
      putchar(dq.front());
      dq.pop_front();
    }
    putchar('\n');
  }
  return 0;
}