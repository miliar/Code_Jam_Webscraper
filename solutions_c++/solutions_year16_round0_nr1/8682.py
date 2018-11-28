#include<bits/stdc++.h>
using namespace std;
bool tab[20];
int main(){
  int test;
  scanf("%d",&test);
  for(int t=1;t<=test;t++){
    printf("Case #%d: ", t);
    for(int i=0;i<10;i++) tab[i]=0;
    int n, ile=0;
    scanf("%d",&n);
    long long p=n;
    while(p){
      long long cc=p;
      while(cc){
	int r=cc%10;
	if(!tab[r]) ile++;
	tab[r]=1;
	cc/=10;
      }
      if(ile==10){
	printf("%lld\n", p);
	break;
      }
      p+=n;
    }
    if(!p) puts("INSOMNIA");
  }   
}