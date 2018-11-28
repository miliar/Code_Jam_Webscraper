#include<cstdio>

using namespace std;

long long p,q;

int main(){
  int tt;
  scanf("%d",&tt);
  for(int c=1;c<=tt;c++){
    scanf("%Ld/%Ld",&p,&q);
    long long t;
    long long a=p;
    long long b=q;
    while(b!=0){
      t=b;b=a%b;a=t;
    }
    //gcd=a;
    p/=a;q/=a;
    bool ans=false;
    bool bbb=false;
    int gen=-1;
    long long g=1;
    for(int i=0;i<=40;i++){
      if(!bbb and p*g>=q){gen=i;bbb=true;}
      if(g==q)ans=true;
      g*=2;
    }
    if(!ans)printf("Case #%d: impossible\n",c);else printf("Case #%d: %d\n",c,gen);
  }
  return 0;
}
