#include <cstdio>
#include <cstring>
char s[113];
int main(){
	int T;
	scanf("%d",&T);
	for (int Case=1;Case<=T;Case++){
		scanf("%s",s);
		int slen=strlen(s);
		bool flip=0;
		int ans=0;
		for (int i=slen-1;i>=0;i--){
			if ((s[i]=='-' && flip==false) || (s[i]=='+' && flip==true)){
				flip^=1;
				ans++;		
			}
		}
		printf("Case #%d: %d\n",Case, ans);
	}
}
