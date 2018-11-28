#include<cstdio>
#include<cstring>

using namespace std;

int main(){
	int t,n;
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	scanf("%d",&t);
	getchar();
	int tests=t;
	char s[101];
	while(t--){
		gets(s);
		bool flipped=false;
		int len=strlen(s);
		int count=0;
		for(int i=len-1;i>=0;i--){
			if(s[i]=='-'){
				if(!flipped){
					count++;
					flipped=true;
				}
			}
			else{//s[i]=='+'
				if(flipped){//actually -
					count++;
					flipped=false;
				}
			}
		}
		printf("Case #%d: %d\n",tests-t,count);
		
	}
	return 0;
}