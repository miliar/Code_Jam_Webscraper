#include <iostream>
#include <stdlib.h>
#include <string.h>
using namespace std;
int compare (const void * a, const void * b)
{
	if ( *(double*)a <  *(double*)b ) return -1;
	if ( *(double*)a == *(double*)b ) return 0;
	if ( *(double*)a >  *(double*)b ) return 1;
}
int main() {
	int test=0;
	cin>>test;
	int test_case=1;
	while(test--){
		int in_size;
		cin>>in_size;
		int deceitful_win_count=0,win_count=0,count=0; 
		double *naomi_input=(double *)malloc(sizeof(double)*in_size);
		memset(naomi_input,0,sizeof(double)*in_size);
		double *ken_input=(double *)malloc(sizeof(double)*in_size);
		memset(ken_input,0,sizeof(double)*in_size);
		
		for(int i=0;i<in_size;i++){
			cin>>naomi_input[i];
		}
		for(int i=0;i<in_size;i++){
			cin>>ken_input[i];
		}
		
		qsort (naomi_input,in_size, sizeof(double), compare);
		
		qsort (ken_input,in_size, sizeof(double), compare);
		int naomi_size=0,ken_size=0;
		while(naomi_size<in_size && ken_size<in_size){
			if(naomi_input[naomi_size]<ken_input[ken_size]){
				naomi_size++;
				ken_size++;
				count++;
			}
			else{
				ken_size++;
			}
		}
		win_count=in_size-count;
		
		naomi_size=0;
		ken_size=0;
		
		while(naomi_size<in_size && ken_size<in_size){
			if(naomi_input[naomi_size]<ken_input[ken_size]){
				naomi_size++;
			}
			else{
				naomi_size++;
				ken_size++;
				deceitful_win_count++;
			}
		}
		cout<<"Case #"<<test_case<<": "<<deceitful_win_count<<" "<<win_count<<endl;
		test_case++;
		free(ken_input);
		ken_input=NULL;
		free(naomi_input);
		naomi_input=NULL;
	}
	return 0;
}