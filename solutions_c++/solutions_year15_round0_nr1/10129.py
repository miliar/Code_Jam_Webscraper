#include <iostream>
#include<stdio.h>
using namespace std;

int main() {
	// your code goes here
	int t,T;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		int sMax;
		scanf("%d",&sMax);	
		int i,op=0;
		char input[sMax+1];
		scanf("%s",input);
		long people=0;
		//if(people==0)op=1;op=0;
		
		for(i=0;i<=sMax;i++){
			
			if(input[i]-'0'>0 && people<i){
				
				int temp = i-people;
				people+=temp;
				op+=temp;
			}{
			people+=(input[i]-'0');
			}
		
		}
		
	printf("Case #%d: %d\n",t,op);	
	}
	return 0;
}
