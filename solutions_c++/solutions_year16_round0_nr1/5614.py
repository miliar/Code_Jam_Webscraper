#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define LEN 10000000

char str[LEN];
bool lst[10];
int count;
int curr, temp1, temp2;

void addnum(){
  for(int i=0;i<strlen(str);i++){
    if(!lst[str[i]-'0']){
      lst[str[i]-'0']=true;
      count--;
    }
  }
}

void initlst(){
  for(int i=0;i<10;i++) lst[i]=false;
}

int main(int argc, char const *argv[]) {
  int n;
  scanf("%d\n", &n);
  for(int i=0;i<n;i++){
    scanf("%d\n", &curr);
    printf("Case #%d: ", i+1);
    if(curr==0){
      printf("INSOMNIA\n");
    }else{
      temp1=0;
      count=10;
      initlst();
      while(count){
        temp1++;
        temp2=curr*temp1;
        str[0]='\0';
        snprintf(str, LEN, "%d", temp2);
        addnum();
      }
      printf("%d\n", temp2);
    }
  }
  return 0;
}
