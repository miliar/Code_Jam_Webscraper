#include<cstdio>
#include<iostream>
using namespace std;
int main(){
long int t,smax,caseno=1;
char s[10000];
scanf("%ld",&t);
	while(t--){
			scanf("%ld",&smax);
			scanf("%s",s);
			long int count=0,need=0;
			if(smax==0){printf("Case #%ld: 0\n",caseno++);continue;}
			else{
				
				for(int i=0;i<=smax;i++){
					//cout<<count<<" "<<i<<" "<<s[i]<<" "<<need<<endl;
					if(i>count && s[i]!='0'){
						need+=(i-count);
						count+=(i-count);
					}
					count+=s[i]-'0';
				}
				printf("Case #%ld: %ld\n",caseno++,need);
			}
			
	}
}
