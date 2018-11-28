#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <string.h>
#include <queue>
#include <vector>
#include <math.h>

using namespace std;

int main(){
	int tc;
	scanf("%d",&tc);

	FILE *f;

	f=fopen("a.txt","w");
	for(int a=0;a<tc;a++){

		int S;
		scanf("%d",&S);

		char arr[1005]={0};
		scanf("%s",arr);

		int standing=0;
		int friends=0;
		standing+=arr[0]-'0';

		for(int i=1;i<=S;i++){
			while(standing<i){
				friends++;
				standing++;
			}
			standing+=arr[i]-'0';
		}

		fprintf(f,"Case #%d: %d\n",a+1,friends);
	}
	fclose(f);
}