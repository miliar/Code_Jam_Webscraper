#include<iostream>
#include<cstdio>
#include<cstring>

using namespace std;
int num[20];
int t, n,tmp;
int v[10];
void cut(int n){
	int i=0;
	int w=n;
	while(w){
		int a=w%10;
		w/=10;
		v[a]++;
	}
}
void zz(){
	tmp=n;
	while(1){
	//	cout<<tmp<<endl;
		cut(tmp);
		int ok=0;
		for(int i=0 ; i<10 ; i++){
			if(!v[i]){
				ok=1;
				break;
			}
		}
		if(!ok) break;
		tmp+=n;
	}
	printf("%d\n",tmp);
}
int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);	
	for(int i=1 ; i<=t ; i++){
		scanf("%d",&n);
		memset(num,0,sizeof(num));
		memset(v,0,sizeof(v));
		printf("Case #%d: ",i);
		if(!n) printf("INSOMNIA\n");
		else{
			zz();
		}
	}
	return 0;
}
