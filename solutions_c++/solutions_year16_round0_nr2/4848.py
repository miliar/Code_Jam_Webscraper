#include <cstdio>
#include <string>

int main(){
	int T,Case=1,cnt;
	char s[105];
	std::string S;
	scanf("%d",&T);
	getchar();
	while(T--){
		gets(s);
		S=s;
		cnt=0;
		for(int i=S.size()-1;i>=0;i--){
			if(S[i]=='-'){
				for(int j=i;j>=0;j--){
					if(S[j]=='+'){
						S[j]='-';
					}else{
						S[j]='+';
					}
				}
				cnt++;
			}
		}
		printf("Case #%d: %d\n",Case++,cnt);
	}
}