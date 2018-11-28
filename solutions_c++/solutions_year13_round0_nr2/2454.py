#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int a[101][101],MAXx[101],MAXy[101],MIN,MINx,MINy,m,n,T,found,i;
void init(){
  int i,j;
  scanf("%d%d",&n,&m);
  memset(MAXx,0,sizeof(MAXx));
  memset(MAXy,0,sizeof(MAXy));
  for(i=1;i<=n;i++)
	for(j=1;j<=m;j++){
	  scanf("%d",&a[i][j]);
	  MAXx[i]=max(MAXx[i],a[i][j]);
	  MAXy[j]=max(MAXy[j],a[i][j]);
	}
}
void findmin(){
  int i,j;
  MIN=101;
  for(i=1;i<=n;i++)
	for(j=1;j<=m;j++)
	  if(a[i][j]<MIN){
		MIN=a[i][j];
		MINx=i;MINy=j;
	  }
}
void findline(){
  int flag,i;
  found=0;
  flag=1;
  for(i=1;i<=n;i++)
	if(a[i][MINy]!=MIN){
	  flag=0;
	  break;
	}
  if(flag){
	found=1;
	return;
  }
  flag=1;
  for(i=1;i<=m;i++)
	if(a[MINx][i]!=MIN){
	  flag=0;
	  break;
	}
  if(flag){
	found=2;
	return;
  }
}
void fill(){
  int i;
  if(found==1){
	for(i=1;i<=n;i++)
	  a[i][MINy]=max(MAXx[i],MAXy[MINy]);
  }
  else{
	for(i=1;i<=m;i++)
	  a[MINx][i]=max(MAXx[MINx],MAXy[i]);
  }
}
int update(){
  int i,j,flag=1;
  for(i=1;i<=n;i++)
	for(j=1;j<=m;j++){
	  if(a[i][j]!=a[1][1])flag=0;
	  MAXx[i]=max(MAXx[i],a[i][j]);
	  MAXy[j]=max(MAXy[j],a[i][j]);
	}
  if(flag)return(1);
  return(0);
}
void solve(){
  while(1){
	findmin();
	findline();
	if(found==0){
	  printf("NO\n");
	  return;
	}
	fill();
	if(update())break;
  }
  printf("YES\n");
}
int main(){
  freopen("b.in","r",stdin);
  freopen("b.out","w",stdout);
  scanf("%d",&T);
  for(i=1;i<=T;i++){
	init();
	printf("Case #%d: ",i);
	solve();
  }
  fclose(stdin);
  fclose(stdout);
  return(0);
}
