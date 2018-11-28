#include<cstdio>

using namespace std;

int main()
{
  int T;
  scanf("%d", &T);

  for(int i=0;i<T;i++){
    printf("Case #%d: ", i+1);
    int X, R, C;

    scanf("%d%d%d", &X, &R, &C);

    int min=(R<C)?R:C;
    int max=(R>C)?R:C;

    if((R*C)%X)
      goto out;
    if(X>max)
      goto out;
    if((X-min)>min)
      goto out;
    if(X==4){
      if(min<3)
        goto out;
      //if(min<4 && max<8)
       // goto out;
    }

    printf("GABRIEL\n");
    continue;
out:
    printf("RICHARD\n");
  }
}
