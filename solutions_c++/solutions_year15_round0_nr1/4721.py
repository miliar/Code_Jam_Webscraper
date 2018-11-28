#include <cstdio>
#include <algorithm>
int ans(int s_max, char audience[]){
  int stand = 0, require_max = 0;
  for(int i = 0;audience[i];++i){
    if(i > stand){
      require_max = std::max(require_max, i - stand);
    }
    stand += audience[i] - '0';
  }
  return require_max;
}

int main(){
  int T;
  scanf("%d", &T);
  for(int i = 1;i <= T;++i){
    int s_max;
    char audience[1002];
    scanf("%d%s", &s_max, audience);
    printf("Case #%d: %d\n", i, ans(s_max, audience));
  }
}
