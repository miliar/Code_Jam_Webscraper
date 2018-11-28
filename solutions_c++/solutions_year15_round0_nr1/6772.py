#include <cstdlib>
#include <cstdio>

int main(){
	int T, cases = 1;
	scanf("%d\n", &T);
	while(T--){
		int shyLevel;
		int friends = 0;
		char input[2*1024];
		int standing = 0;
		scanf("%d %s\n", &shyLevel, input);
		//printf("@@%d %s\n", shyLevel, input);
		standing = input[0]-'0';
		for(int i=1; i<=shyLevel; i++){
			//printf("%d %d %d\n", friends, standing, input[i]-'0');
			if(standing < i){
				int need = i - standing;
				friends += need;
				standing += need;
			}
			standing += input[i] - '0';
		}
		
		
		printf("Case #%d: %d\n", cases++, friends);
	}
	return 0;
}

