#include<bits/stdc++.h>
using namespace std;
vector<int>v;
int rozdaj(int x){
   int ile=0;
   for(int i=0;i<v.size();i++){
      if(v[i]>x){
	 if(v[i]%x==0)
	    ile+=v[i]/x-1;
	 else
	    ile+=v[i]/x;
      }
   }
   return ile;
}
int main(){
   int T;
   scanf("%d",&T);
   
   for(int t=1;t<=T;t++){
      int n;
      scanf("%d",&n);
      
      v.resize(0);
      v.resize(n);
      int size=0;
      for(int i=0;i<n;i++){
	 scanf("%d",&v[i]);
	 size=max(size,v[i]);
      }
      
      int odp=size;
      for(int i=1;i<size;i++){
	 int god=rozdaj(i);
	 odp=min(god+i,odp);
      }
      printf("Case #%d: %d\n",t,odp);
   }
   return 0;
}