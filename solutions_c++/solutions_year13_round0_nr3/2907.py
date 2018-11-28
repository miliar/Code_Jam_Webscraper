#include <cstdio>
//int[] a = [1,4,9,121,484];
int t,a,b;
int main(){
  scanf("%d",&t);
    for(int i=0;i<t;i++){
    int n=5;
    scanf("%d %d",&a,&b);
    if(a>1) n--;
    if(a>4 || b< 4) n--;
    if(a>9 || b< 9) n--;
    if(a>121 || b< 121) n--;
    if(a>484 || b< 484) n--;    
    
    printf("Case #%d: %d\n",i+1,n);
    }
}
