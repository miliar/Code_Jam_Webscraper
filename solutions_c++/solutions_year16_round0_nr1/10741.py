#include<cstdio>

int main() {
  int t;
  int num,temp,temp2;
  int check = 0;
  int used,ans;
  int summary = (1 << 10) - 1;

  scanf("%d", &t);
  // printf("summary %d",summary);

  for(int i = 0 ; i < t; i++) {
    scanf("%d",&num);
    check = 0;
    ans = -1;
    for(int j = 1 ; j < 1000 ; j++) {
      temp = num * j;
      while(temp > 0) {
        temp2 = temp % 10;
        used = 1 << temp2;
        check |= used;
        temp = temp / 10;
      }

      // printf("check %d\n",check);

      if(check == summary) {
        ans = num * j;
        break;
      }
    }

    if(ans != -1) {
      printf("Case #%d: %d\n",i+1,ans);
    }else {
      printf("Case #%d: INSOMNIA\n",i+1);
    }
  }

  return 0;
}
