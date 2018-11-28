#include <cstdio>
#include <iostream>
#include <cstdlib>
using namespace std;

int main(){
	int cas;
	int test=0;
	
	scanf("%d",&cas);
	for(int i=0;i<cas;i++){
		int level = 0;
		scanf("%d",&level);
		int cnt = 0;
		int temp = 0;
		char* aud;
		aud = (char *)malloc(sizeof(char)*(level+1));
		scanf("%s",aud);
		//printf("%s",aud);
		if(level == 0){
			printf("Case #%d: 0",i+1);
			printf("\n");
			}
		else{
			temp = (aud[0]-48);
			for(int j = 1; j<(level+1);j++){
				if(aud[j]!=48){
					if(temp>=j) temp+=(aud[j]-48);
					else{
						while(1){
							temp++;
							cnt++;
							if(temp == j){
								temp+=(aud[j]-48);
								break;
								}
							}
						}
					}
				}
			printf("Case #%d: %d",i+1,cnt);
			printf("\n");
			}
		}
	
	return 0;
	}
