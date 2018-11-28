#include<bits/stdc++.h>
using namespace std;
char x[10][10];
vector<int>v[10];
int ile[5], tab[10][10], on[5], nr[5];
int n;
int p(int a){
  if(nr[a]!=a) nr[a]=p(nr[a]);
  return nr[a];
}

int f(int kto){
  int maxi=100;
  if(kto==n+1){
//     for(int i=1;i<=n;i++){
//       for(int j=0;j<n;j++) printf("%d ", tab[i][j]);
//       puts("");
//     }
//     puts("-----");
    int add=0;
  
    for(int i=1;i<=n;i++) on[i]=ile[i]=0;

    for(int j=1;j<=n;j++){ //umiejetnosci
      for(int i=1;i<=n;i++) {
	ile[j]+=tab[i][j];
	on[i]+=tab[i][j];
      }
    }
    for(int i=1;i<=n;i++){
      if(on[i]==0) return 100;
      for(int j=1;j<=n;j++){
	if(x[i][j]=='1' and tab[i][j]==0) return 100;
	if(x[i][j]=='0' and tab[i][j]==1) add++;
	if(tab[i][j]){
	  if(on[i]!=ile[j]) return 100;
	}
	for(int k=j+1;k<=n;k++){
	  if(p(j)==p(k) and tab[i][j]!=tab[i][k]) return 100;
	}
      }
    }
//     for(int i=1;i<=n;i++){
//       for(int j=1;j<=n;j++) printf("%d ", tab[i][j]);
//       puts("");
//     }
//     puts("-----");
//     printf("add %d\n", add);
    return add;
  }
  for(int opt=0;opt<(1<<n);opt++){
    int r=opt;
    for(int j=1;j<=n;j++){
      tab[kto][j]=r%2;
      r/=2;
    }
    maxi=min(maxi, f(kto+1));
  }
  return maxi;
}
int u(int a,int b){
  if(p(a)!=p(b)){
    nr[nr[a]]=nr[nr[b]];
  }
}
int main(){
  int test;
  scanf("%d",&test);
  for(int t=1;t<=test;t++){
    int ans=0;
    for(int i=1;i<=n;i++) nr[i]=i;
    printf("Case #%d: ", t);
    scanf("%d",&n);
    for(int i=1;i<=n; i++) {
      scanf(" %s", x[i]+1);
      for(int j=1;j<=n;j++){
	for(int k=j+1;k<=n;k++)
	  if(x[i][j]=='1' and x[i][k]=='1') u(j,k);
      }
    }
    for(int i=1;i<=n;i++) v[p(i)].push_back(i);
    for(int i=1;i<=n;i++){ //gosc
      for(int j=1;j<=n;j++){ //dla danej grupy
	bool ok=0;
	for(int g=0;g<v[j].size();g++) if(x[i][v[j][g]]=='1') ok=1;
	if(ok) {
	  for(int g=0;g<v[j].size();g++) {
	    if(x[i][v[j][g]]=='0') ans++;
	    x[i][v[j][g]]='1';
	  }
	}
      }
    }
    printf("%d\n", f(1)+ans);
    for(int i=1;i<=n;i++) v[i].clear();
  }
}