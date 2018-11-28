#include <iostream>
#include <cstdio>
#include <string.h>
#define max 1000
#define true 1
#define false 0

using namespace std;


int main(){

	int test;
	int shy_index;
	char shyness[max+10];
	int standing,required;
	int shy_level;
	int i;
	scanf("%d",&test);
	for(int k=0;k<test;k++){
		int no;
		int temp_required;
		scanf("%d",&shy_index);
		scanf("%s",shyness);
		//get_string(shyness);
		/*for(int j=0;j<shy_index;j++)
			scanf("%c",&shyness[j]);*/
		standing =0 ;
		required=0;
		for(i=0;i<=shy_index;i++){
			shy_level=i;
			no=shyness[i]-'0';
			if(shy_level==0){
				standing+=no;
			}
			else{
				if(shy_level > standing){
					 temp_required =  shy_level-standing;
					 required+=temp_required;
					 standing+=temp_required;
					 standing+=no;
				}
				else{
					standing+=no;
				}
			}
		}
		
		printf("Case #%d: %d\n",k+1,required);
	}
}
