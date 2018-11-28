#include "stdio.h"
#include "string"
#include <string.h>
#include "iostream"
using namespace std;

int main(){
	FILE *fp,*out;
	fp = fopen("B-large.in","r");
	out = fopen("Revenge of the Pancakes.txt","w");
	int T,count;
//	scanf("%d",&T);
	fscanf(fp,"%d",&T);
	for(int tc=0;tc<T;++tc){
		char pan[120];
		fscanf(fp,"%s",pan);
//		scanf("%s",pan);
		count = 0;

		int len = strlen(pan);
		if(pan[0]=='+'){
			printf("+ %d",len);
			for(int i=0;i<len-1;++i){
				if(pan[i]=='+' && pan[i+1]=='-'){
					count+=2;
				}
			}
		}else{

			printf("- %d",len);
			++count;
			for(int i=0;i<len-1;++i){
				if(pan[i]=='+' && pan[i+1]=='-'){
					count+=2;
				}
			}
		}

		printf("Case #%d: %d %s\n",tc+1,count,pan);
		for(int i=0;i<100;++i){
			pan[i]=='\0';
		}
		fprintf(out,"Case #%d: %d\n",tc+1,count);

	}
}
