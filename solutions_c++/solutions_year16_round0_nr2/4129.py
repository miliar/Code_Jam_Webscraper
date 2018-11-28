#include <cstdio>
#include <cstdlib>

using namespace std;

int main(){
	int t;
	scanf("%d\n",&t);
	for(int u = 0; u < t; u++){
		printf("Case #%d: ", u + 1);
		char b = '.';
		int count = 0;
		for(char a = getchar(); a != '\n'; a = getchar()){
			if(b == '.') b = a;
			if(a != b) {
				count++;
				b = a;
			}
		}
		if(b == '-'){
			count++;
		}
		printf("%d\n", count);
	}
	return 0;
}
		
