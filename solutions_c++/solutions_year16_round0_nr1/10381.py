#include<bits/stdc++.h>
int digitcounter[10];

bool countandcheckfinal(int n){
  //  printf("checking %d\n", n);
  bool flag;
  int counter;
  while(n){
    digitcounter[n%10]++;
    n = n/10;
  }
  counter = 10;
  flag = true;
  while(counter--){
    if(!digitcounter[counter])
      flag = false;
  }
  return flag;
}

int main(){
  int n,t;
  scanf("%d", &t);
  for(int i=0;i<t;i++){
    scanf("%d",&n);
    if (!n) {
      printf("case #%d: INSOMNIA\n", i+1);
      continue;
    }
    for(int j=0;j<10;j++) digitcounter[j] = 0;
    int counter = 1;
    while(!(countandcheckfinal(n*counter)))
      counter++;
    printf("case #%d: %d\n", i+1, n*counter);
  }
  return 0;
}
