#include<cstdio>
#include<cstring>
int foi[10];
inline void updatedig(int a){
  while(a>0){
    foi[a%10]=1;
    a/=10;
  }
}
inline bool end(){
  for(int i=0;i<10;i++){
    if(foi[i]==0)return false;
  }
  return true;
}
int main(){
  int tt=1;
  scanf("%d",&tt);
  for(int rr=1;rr<=tt;rr++){
    int i;
    scanf("%d",&i);
    printf("Case #%d: ",rr);
    if (i==0){
      printf("INSOMNIA\n");
    }
    else
      {
	memset(foi,0,sizeof(foi));
	int x = i;
	while(true){
	  updatedig(x);
	  if(end())break;
	  x+=i;
	}
	printf("%d\n",x);
      }
  }

  return 0;
}
