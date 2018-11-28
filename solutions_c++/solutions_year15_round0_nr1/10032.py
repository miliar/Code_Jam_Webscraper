#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;
int audTot, sMax, runningGap,  sl[1110];

int main(){
	freopen("opera.in", "r", stdin);
	freopen("opera.out", "w", stdout);
	int TC, T, input;
	scanf(" %d", &TC);
	for (T = 1; T <= TC; T++){
		printf("Case #%d: ", T);
		audTot = 0;
		
		scanf("%d", &sMax); 
		scanf("%d", &input);
		
		for(int i = sMax; i >=0; i--){
			sl[i] = input%10; input /= 10;
			audTot+=sl[i];
		}
		
		int friends = 0;
		int standing = 0;
		int stepper = 0;
		
		while(stepper <= sMax){
			while(stepper <= standing){
				standing += sl[stepper];
				stepper++; if(standing==audTot){goto allUp;}
			}
			
			if(standing<audTot){
				standing+=sl[stepper]; stepper++; friends++; audTot++; standing++;
			}
			
		}
		allUp:
		
		
		printf("%d\n", friends);
		
	}
	return 0;
}
