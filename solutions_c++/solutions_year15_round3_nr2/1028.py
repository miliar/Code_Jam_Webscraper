#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#define mp(a,b) make_pair((a),(b))
#define ff first
#define ss second

using namespace std;

int maxi(int a, int b){
  if(a>=b){
    return a;
  }
  return b;
}

int main(){
  int i,j,k,l,m,n,o,p,r,s,t,T;
  int b_max, b_total, b_try, ok;
  double res;
  char c;
  vector<char> slovo, target, keyboard;
  
  scanf("%d",&T);
  
  for(t=1;t<=T;t++){
    scanf("%d",&k);
    scanf("%d",&l);
    scanf("%d",&s);
    
    slovo.clear();
    target.clear();
    keyboard.clear();
    
    for(i=0;i<k;i++){
      c=getchar();
      while(c=='\n'){
        c=getchar();
      }
      keyboard.push_back(c);
    }
    
    for(i=0;i<l;i++){
      c=getchar();
      while(c=='\n'){
        c=getchar();
      }
      target.push_back(c);
    }
    
    p=1;
    for(i=0;i<s;i++){
      p*=k;
    }
    
    slovo.resize(s);
    
    b_max=0;
    b_total=0;
    
    /*printf("Keys: %d\n",k);
    printf("String lenght: %d\n",s);
    printf("Target lenght: %d\n",l);
    printf("Pokusy: %d\n",p);*/
    
    for(i=0;i<p;i++){
      m=i;
      for(j=0;j<s;j++){
        slovo[j]=keyboard[m%k];
        m/=k;
      }
      b_try=0;
      for(j=0;j<=(s-l);j++){
        ok=1;
        for(o=0;o<l;o++){
          if(target[o]!=slovo[j+o]){
            ok=0;
            break;
          }
        }
        if(ok){
          b_try++;
        }
      }
      b_total += b_try;
      b_max = maxi(b_max,b_try);
    }
    
    res = ((double)(b_max*p-b_total))/((double)p);
    
    printf("Case #%d: %.20lf\n",t,res);
  }
  
  return 0;
}