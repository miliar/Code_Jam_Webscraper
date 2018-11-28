#include <bits/stdc++.h>
#include <string.h>
using namespace std;

int main(){
	int n;

	scanf("%d",&n);

	char input[10002];
	char arr[6002];

	for(int i=0;i<n;i++){
		scanf("%s",&input);

		char arr[6002];
		int start=2000,last=2000;
		char cs=input[0],cl=input[0];
		arr[2000]=cs;
		
		//printf("char-  %c \n", input[0]);

		for(int j=1;j<strlen(input);j++){


			if(input[j]>=cs){
				arr[--start]=input[j];
				cs=input[j];

			}else{
				arr[++last]=input[j];
				cl=input[j];
			}

		}

		printf("Case #%d: ",i+1 );
		for(int j=start;j<=last;j++){
			printf("%c",arr[j] );
		}

		printf("\n");
	}
	
}