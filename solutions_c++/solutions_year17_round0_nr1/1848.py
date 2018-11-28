#include<stdio.h>
#include<string>

void solve(){
  char tmp[1042];
  scanf(" %s ", tmp);
  std::string s = tmp;
  int K; scanf("%d", &K);
  int cnt = 0;
  int pos = 0;
  for(;pos<=int(s.length())-K; pos++){
    if(s[pos]=='-'){
      for(int j=pos; j<pos+K; j++)
        s[j] = (s[j]=='-' ? '+' : '-');
      cnt++;
    }
  }
  while(pos < s.length()){
    if(s[pos++]!='+'){
      printf("IMPOSSIBLE\n");
      return;
    }
  }
  printf("%d\n", cnt); 
}

int main(int agrc, char*argv[]){
  int T; scanf("%d", &T);
  for(int tc=1; tc<=T; tc++){
    printf("Case #%d: ", tc);
    solve();
  }
  return 0;
}
