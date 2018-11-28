#include <bits/stdc++.h>

#define inf 0x3f3f3f3
#define maxn 1000010

char a[maxn],b[maxn];
int main(){
  int test;
  scanf("%d",&test);
  for(int t=0;t<test;t++){
    scanf("%s %s",a,b);
    int len=strlen(a);
    int i,j;
    int pot=1;
    for(int i=0;i<len;i++){
      pot *=10;
    }
    int ax,by,bs=inf;
    int aux,auy;
    for(i=0;i<pot;i++){
      for(j=0;j<pot;j++){
	aux=i;
	auy=j;
	//if(i!=123&&j!=123)continue;
	int ok=1;
	for(int k=len-1;k>=0;k--){
	  int ar=aux%10;
	  aux/=10;
	  if(a[k]!=('0'+ar)&&a[k]!='?'){
	    ok=0;
	    break;
	  }
	  int br=auy%10;
	  auy/=10;
	  if(b[k]!=('0'+br)&&b[k]!='?'){
	    ok=0;
	    break;
	  }
	}
	if(bs>abs(i-j)&&ok){
	  bs=abs(i-j);
	  ax=i;
	  by=j;
	}
      }
    }
    // printf("%d %d\n",ax,by);
    for(int k=len-1;k>=0;k--){
      int ar=ax%10;
      ax/=10;
      a[k]=ar+'0';
      int br=by%10;
      by/=10;
      b[k]=br+'0';
	
    }
    printf("Case #%d: %s %s\n",t+1,a,b);
  }
  return 0;
}
