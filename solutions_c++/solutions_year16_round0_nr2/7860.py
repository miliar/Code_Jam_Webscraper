#include<cstdio>
#include<cstring>

int main(){

	int T;
	scanf("%d",&T);
	
	for(int i=0;i<T;i++){
		char s[101];
		scanf("%s",s);
		int last = strlen(s);
		int flip=0;
		
		for(int j=0;j<last-1;j++){
			if(s[j]==s[j+1]){
				
			}else flip++;
		}
		if(s[last-1]=='-'){
			flip++;
		}
		printf("Case #%d: %d\n",i+1,flip);
	}
	return 0;
}
