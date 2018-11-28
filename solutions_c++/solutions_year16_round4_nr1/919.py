#include<bits/stdc++.h>
using namespace std;
int tab[5005], ile[3], taken[3];
int f(int co, int n, int poz){
//   printf("f %d %d %d\n", co, n, poz);
  if(n==1){
    tab[poz]=co;
    taken[co]++;
    return 0;
  }
  int los=(co+1)%3;
  f(co, n/2, poz);
  f(los, n/2, poz+n/2);
  
}
int main(){
  string aa[3],ans;
  int test;
  scanf("%d",&test);
  for(int t=1;t<=test;t++){
    cout<<"Case #"<<t<<": ";
//     printf("Case #%d: ", t);
    int n, ok=0;
    scanf("%d",&n);
    for(int i=0;i<3;i++) scanf("%d", &ile[i]);
    swap(ile[0],ile[1]);//P R S
    for(int i=0;i<3;i++){
      f(i,(1<<n),0);
      int maybe=1;
      for(int j=0;j<3;j++) {
	if(taken[j]!=ile[j]) maybe=0;
	taken[j]=0;
      }
      if(maybe){
	for(int j=0;j<n;j++){
	  for(int k=0;k<(1<<n);k+=2*(1<<j)){
	    for(int g=k; g<k+(1<<j);g++){
	      if(tab[g]>tab[g+(1<<j)]) {
		for(int m=k, e=k+(1<<j);m<k+(1<<j);m++, e++) swap(tab[m], tab[e]);
		 break;
	      }
	      if(tab[g]<tab[g+(1<<j)]) break;
	    }
	  }
	}
	for(int j=0;j<(1<<n);j++) {
	  if(tab[j]==0) aa[i]+="P";//printf("P");
	  if(tab[j]==1) aa[i]+="R";//printf("R");
	  if(tab[j]==2) aa[i]+="S";//printf("S");
	}
	ans=aa[i];
	ok=1;
      }
      else aa[i]+="#";
    }
    if(!ok)cout<<"IMPOSSIBLE"<<"\n";//puts("IMPOSSIBLE");
    else{      
      for(int i=0;i<3;i++) if(aa[i][0]!='#' and aa[i]<ans) ans=aa[i];
      cout<<ans<<"\n";
    }
    for(int i=0;i<3;i++) aa[i].clear();
  }
  return 0;
}