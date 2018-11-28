#include <cstdio>
#include<cstring>
char ent[1234];
int main(){
  int tt;
  scanf("%d",&tt);
  for(int rr=1;rr<=tt;rr++){
    scanf(" %s",ent);
    int tam = strlen(ent);
    ent[tam]='+';
    int ret = 0;
    for(int i=0;i<tam;i++){
      if(ent[i]!=ent[i+1])ret++;
    }
    printf("Case #%d: %d\n",rr,ret);
  }
  return 0;
}
