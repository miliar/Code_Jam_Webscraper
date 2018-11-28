#include <cstdio>
#include <cstring>

using namespace std;

int main(){
	int t;
	scanf("%d",&t);
	for(int index = 1;index <= t;index++){
		char a[110];
		scanf("%s",a);
		int len = strlen(a);
		int ans = 0;
		char check = a[0];
		for(int i = 0; i < len; i++){
			if(a[i]!=check){
				ans++;
				check = a[i];
			}
		}
		if(a[len-1]=='-'){
			ans++;
		}
		
		printf("Case #%d: %d\n",index,ans);
	}
	return 0;
}