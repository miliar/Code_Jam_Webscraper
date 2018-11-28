#include<cstdio>
#include<algorithm>
#include<map>
#include<cassert>
#include<cstring>
using namespace std;
int n;
int val[1234];
int aux[1234];
int pos[1234];
map<int,int> dict;

int best[1234][1234];

int main () {
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++){
    scanf("%d",&n);
    dict.clear();
    memset(best,-1,sizeof(best));
    for(int i=0;i<n;i++){
      scanf("%d",&val[i]);
      aux[i]=val[i];
    }
    sort(aux,aux+n);

    for(int i=0;i<n;i++)
      dict[aux[i]]=i;
    
    
    for(int i=0;i<n;i++){
      pos[dict[val[i]]]=i;
      val[i]=dict[val[i]];
    }
    
    int ret=999999999;
    for(int i=0;i<(1<<n);i++){
      int at = 0;
      for(int j=0;j<n;j++)
	aux[j]=val[j];
      aux[n]=-1;

      for(int k=0;k<n;k++){
	int inv = 0;
	int p;
	for(int j=0;j<n;j++){
	  if(aux[j]==k)p=j;
	}
	if (i & (1<<k)){
	  inv = 1;
	}
	//	if(i==(0 + 2 + 4 + 0 + 0))
	//	  printf("%d %d\n",i,p);

	if(inv ==0){
	  while(p>0 && aux[p-1]>aux[p]){
	    swap(aux[p],aux[p-1]);
	    p--;
	    at++;
	  } 
	}
	else{
	  while(aux[p]<aux[p+1]){
	    swap(aux[p],aux[p+1]);
	    p++;
	    at++;
	  }
	  
	}
	//	if(i==(0 + 2 + 4 + 0 + 0))printf("%d %d>\n",at,inv);
      }
      ret = min(ret,at);
    }
    
    
    printf("Case #%d: %d\n",pp,ret);
  }
  return 0;
}
