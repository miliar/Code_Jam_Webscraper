#include <bits/stdc++.h>
using namespace std;
bool S[110];
string st;
void flip(int idx){
  for(int i = 0; i <= idx; i++)
    S[i] = S[i]?false:true;
}

void show(){
  for(int i = 0; i < st.size(); i++)
    printf("%c",S[i]?'+':'-');
  putchar('\n');
}

int main(){
  int T;
  cin >> T;
  for(int C = 1; C <= T; C++){
    int cont = 0;
    cin >> st;
    for(int i = 0; i < st.size(); i++){
      S[i] = (st[i] == '+') ? true : false;
    }
    for(int i = st.size()-1; i >= 0; i--){
      if(!S[i]) {
        flip(i);
        cont++;
        //show();
      }
    }
    printf("Case #%d: %d\n",C,cont);
  }
  return 0;
}