#include <iostream>
#include <cstdio>
using namespace std;

int Correct[11]={1,2,4,8,16,32,64,128,256,512,1024};

int main(){
	int T; scanf("%d",&T);
	for(int Case=1; Case<=T; ++Case){
		int a,b;
		scanf("%d/%d",&a,&b);
		if(a==b){
			printf("Case #%d: %d\n",Case,0);
			continue;
		}
		bool Find=false;
		for(int i=0; i<10; ++i){
			if(b==Correct[i]) Find=true;
		}
		if(!Find){
			printf("Case #%d: impossible\n",Case);
			continue;
		}
		int ans=0;
		while(a<b){
			++ans;
			if(b%2==0) b/=2;
			else{ ans=-1; break;}
		}
		if(ans!=-1)
			printf("Case #%d: %d\n",Case,ans);
		else
			printf("Case #%d: impossible\n",Case);
	}
	return 0;
}
