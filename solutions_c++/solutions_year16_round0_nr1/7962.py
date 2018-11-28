#include<cstdio>
#include<iostream>

using namespace std;
bool vi[10];
bool check(){
	for(int j=0;j<10;j++){
		if(vi[j]==false)return false;
	}
	return true;
}
int main(){
	//freopen("A-large.in","r",stdin);
	//freopen("A-small-attempt0.out","w",stdout);
	int t,n;
	long long int tmp,ans;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		scanf("%d",&n);
		if(n==0){
			printf("Case #%d: INSOMNIA\n",i+1);
		}else{
			for(int j=0;j<10;j++){
				vi[j]=false;
			}
			tmp=n;
			while(!check()){
				ans=tmp;
				while(ans>0){
					vi[(ans%10)]=true;
					ans=ans/10;
				}
				tmp=tmp+n;
			}
			printf("Case #%d: %lld\n",i+1,tmp-n);
		}
		
	}
	
	
	return 0;
}
