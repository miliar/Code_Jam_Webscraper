#include <cstdio>

char in[1024];

int main(){
  int T;
  int s;
  int i;
  int count;
  int ans;

  scanf("%d", &T);
  for(int tt = 0; tt < T; tt++){
    scanf("%d", &s);
    scanf("%s", in);

    ans = count = 0;
    for(i = 0; i <= s; i++){
      if(count + ans < i)
	ans += i - (count + ans);
      
      count += in[i] - '0';
    }
    printf("Case #%d: %d\n", tt + 1, ans);
  }
}
