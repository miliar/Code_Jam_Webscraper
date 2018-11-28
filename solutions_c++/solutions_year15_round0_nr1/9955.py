#include <iostream>
#include <cstdio>

using namespace std;

int main() {
	int T, tcase = 0;
	scanf("%d", &T);
	
	while(T--){
		int S;
		scanf("%d", &S);
		
		char audi[S+10];
		scanf("%s", audi);
		
		int invited = 0, claping = (audi[0]-'0');
		
		for(int i=1; i<=S; i++){
			if(claping < i){
				invited += (i - claping);
				claping = i;
			}
			
			claping += (audi[i]-'0');
		}
		
		printf("Case #%d: %d\n", ++tcase, invited);
	}
}