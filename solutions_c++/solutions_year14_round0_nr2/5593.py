#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#define mp(a,b) make_pair((a),(b))
#define ff first
#define ss second

using namespace std;

int main(){
  int i,j,k,l,n,o,t;
  int b,e,mid;
  double p,r,s,m,c,f,x;
  
  scanf("%d",&t);
  
  for(l=0;l<t;l++){
    scanf("%lf",&c);
    scanf("%lf",&f);
    scanf("%lf",&x);
    
    m=x/(double)2;
    
    b=0;
    e=x/c+2;
    
    while(e-b>1){
      mid=(b+e)/2;
      r=(double)2;
      s=(double)0;
      for(i=0;i<mid;i++){
	s+=c/r;
	r+=f;
      }
      s+=x/r;
      
      r=(double)2;
      p=(double)0;
      for(i=0;i<mid-1;i++){
	p+=c/r;
	r+=f;
      }
      p+=x/r;
      
      if(s<p){
	b=mid;
      }else{
	e=mid;
      }
    }
    
    mid=b;
    r=(double)2;
    s=(double)0;
    for(i=0;i<mid;i++){
      s+=c/r;
      r+=f;
    }
    s+=x/r;
    printf("Case #%d: %.10f\n",l+1,s);
  }
  
  return 0;
}
