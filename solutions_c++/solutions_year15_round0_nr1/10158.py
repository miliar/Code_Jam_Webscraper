/*

	Problem A: Standing Ovation
	Author: Shreedhar
	
*/

#include<stdio.h>
int main(){
	
	int t, T, noOfStoodAud, frndsInvited, newFrnds, curShy, maxShyness;
		char shyPeople[1001];
		scanf("%d",&T);
		for(t = 0; t < T; t++){
			
			frndsInvited = 0;
			noOfStoodAud = 0;
			curShy = 0;
			
			scanf("%d %s", &maxShyness, shyPeople);
			
			while(curShy <= maxShyness){
				newFrnds = 0;
				if(curShy > noOfStoodAud){
					newFrnds = curShy - noOfStoodAud;
					frndsInvited += newFrnds;
				}
				noOfStoodAud += newFrnds + (shyPeople[curShy]-48);
				curShy++;
			}
			
			printf("Case #%d: %d\n", t+1, frndsInvited);
		}
	
	return 0;
}
