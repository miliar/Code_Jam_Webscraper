#include<cstdio>

using namespace std;

int main(void)
{
  int T;
  scanf("%d", &T);
  for(int i=0;i<T;i++){
    int S;
    scanf("%d", &S);
    int c=0;
    int inv=0;
    char x;
    scanf("%c", &x);

    for(int j=0;j<S+1;j++){
      scanf("%c", &x);
      x-='0';
      //printf("read %d\n", x);

      if(c<j){
        inv+=j-c;
        c+=j-c;
      }
      c+=x;
    }

    printf("Case #%d: %d\n", i+1, inv);
  }
}
