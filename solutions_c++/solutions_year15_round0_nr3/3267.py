#include <stdio.h>

int arr[4][4]={{ 1, 2, 3, 4},
	       { 2,-1, 4,-3},
	       { 3,-4,-1, 2},
	       { 4, 3,-2,-1}};

bool search(int str[],int a,int l,int x,int s){
  if(s==2){
    bool pos=true;
    int i=a;
    int cur=1;
    do{
      for(;i<l;i++){
	cur=arr[cur-1][str[i]-1];
	//printf("blah %d %d %d blah\n",cur,str[i],i);
	if(cur<0){
	  pos=!pos;
	  cur=cur-2*cur;
	}
	if(pos && cur==2){
	  //printf("%d asdasdi\n",i);
	  if(search(str,i+1,l,x,3))
	    return true;
	}
      }
      i=0;
    }while(--x);
  }
  if(s==3){
    bool pos=true;
    int i=a;
    int cur=1;
    do{
      for(;i<l;i++){
        //printf("blah %d %d %d blah\n",cur,str[i],i);
	cur=arr[cur-1][str[i]-1];
	if(cur<0){
	  pos=!pos;
	  cur=cur-2*cur;
	}
	if(pos && cur==3){
	  //printf("%d asdasdj\n",i);
	  if(search(str,i+1,l,x,4))
	    return true;
	}
      }
      i=0;
    }while(--x);
  }
  if(s==4){
    bool pos=true;
    int i=a;
    int cur=1;
    do{
      for(;i<l;i++){
	cur=arr[cur-1][str[i]-1];
	if(cur<0){
	  pos=!pos;
	  cur=cur-2*cur;
	}
      }
      i=0;
    }while(--x);
    if(pos && cur==4)
      return true;
  }
  return false;
  
}

int main(){
  int t,n,l,x,cur,i,c,k;
  int str[10000];
  char strc[10001];
  scanf("%d",&t);
  for(k=1;k<=t;k++){
    scanf("%d%d",&l,&x);
    scanf("%s",strc);
    for(i=0;i<l;i++){
      c=strc[i];
      if(c=='i')
	str[i]=2;
      if(c=='j')
	str[i]=3;
      if(c=='k')
	str[i]=4;
    }
    if(search(str,0,l,x,2))
      printf("Case #%d: YES\n",k);
    else
      printf("Case #%d: NO\n",k);
  }
  return 0;
}
