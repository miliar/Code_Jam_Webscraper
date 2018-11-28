#include <bits/stdc++.h>
using namespace std;
inline bool valida(vector<bool> v){
	for(int i=0;i<10;i++)if(v[i]==0)return 0;
	return 1;
}
inline int f(int n){
	vector<bool> v(10,false);
	int pos=1;
	while(1){
		int aux=n*pos;
		while(aux>0){
			v[aux%10]=1;
			aux/=10;
		}
		if(valida(v))return n*pos;
		pos++;
	}
	
}
int main(){
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		int x;
		scanf("%d",&x);
		if(x!=0){
			printf("Case #%d: %d\n",i+1,f(x));
		}else{
			printf("Case #%d: INSOMNIA\n",i+1);		}
	}
	return 0;
}


