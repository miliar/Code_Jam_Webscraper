#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int M[101][101];
bool revisar(int,int);
int cont;
int R,C;
int main(){
	int t; scanf("%d\n",&t);
	for(int caso=1;caso<=t;caso++){
		scanf("%d %d\n",&R,&C);
		for(int i=0;i<R;i++) for(int j=0;j<C;j++) scanf("%d",M[i]+j);
		bool ans=true;
		for(int i=0;i<R and ans;i++){
			int maxFila=-1;
			for(int j=0;j<C;j++) maxFila=max(maxFila,M[i][j]);
			//cout<<i<<" :"<<maxFila<<endl;
			for(int j=0;j<C and ans;j++){ 
			  if(M[i][j]<maxFila){
			  ans= revisar(j,M[i][j]);
			  }
			}
		}
		printf("Case #%d: %s\n",caso,ans?"YES":"NO");		
	}
return 0;}
bool revisar(int col,int maxVal){
	for(int i=0;i<R;i++){
		if(M[i][col]>maxVal){return false;}
	}
	return true;
}
