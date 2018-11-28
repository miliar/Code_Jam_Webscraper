#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
using namespace std;
int main(){
	long t,n,i,ans,v,count,c=0;
	char s[10000];
	scanf("%ld",&t);
	while(t--){
		++c;
		ans=0;
		count=0;
		scanf("%ld",&n);
		scanf("%s",&s);
		for(i=0;i<strlen(s);i++){
			v=s[i]-'0';
			if(v==0){
				continue;
			}
			else{
					if(count<i){
						ans+=i-count;
						count+=ans;
						count+=v;
					}else{
						count+=v;
					}
			}
		}
		printf("Case #%ld: %ld\n",c,ans);
	}
	return 0;
}
