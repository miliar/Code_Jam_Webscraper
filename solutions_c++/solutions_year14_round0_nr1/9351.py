#include <cstdio>
#include <cstdlib>
#include <string>
#include <algorithm>

using namespace std;

int main(){
	int n;
	scanf("%d", &n);
	
	for(int x = 0; x < n; x++){
		int ans1, ans2, temp;
		scanf ("%d", &ans1);
		int occurences[17] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				scanf("%d", &temp);
				if ((i+1) == ans1){
					occurences[temp]++;
				}
			}
		}
		scanf("%d", &ans2);
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				scanf("%d", &temp);
				if ((i+1) == ans2){
					occurences[temp]++;
				}
			}
		}
		
		int numgreater = 0;
		int finalans;
		for(int i = 0; i < 17; i++){
			if(occurences[i] > 1){
				numgreater++;
				finalans = i;
			}
			//printf("i:%d ", occurences[i]);
		}
		
		if(numgreater == 0){
			printf("Case #%d: Volunteer cheated!\n", x+1);
		} else if (numgreater == 1){
			printf("Case #%d: %d\n", x+1, finalans);
		} else {
			printf("Case #%d: Bad magician!\n", x+1);
		}
	}
	

	
	return 0;
}