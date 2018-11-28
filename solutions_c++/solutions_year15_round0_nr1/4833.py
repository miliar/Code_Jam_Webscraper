#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include<algorithm>
#include <set>
#define MAX_INT 999999
#define LEN 1010
using namespace std;

int main(){
	FILE *fp1,*fp2;
	fp1 = fopen("A-large.in","r");
	fp2 = fopen("A-large.out","w");
	int T,N,L;

	
	fscanf(fp1,"%d",&T);
	//fprintf(fp2,"%d\n",T);
	
	for( int i = 0 ; i < T; i++){
		char li[LEN];
		long long pre[LEN] = {0};
		fscanf(fp1,"%d",&N);
		fscanf(fp1,"%s",li);
	    //fprintf(fp2,"%s\n",li);
	    int res = 0;
	    int len = strlen(li); 
	    pre[1] = li[0] - '0';
	    for( int j = 0 ; j < len ; j++){
	    	int bitnum = li[j] - '0';
	    	pre[j+1] = pre[j] + bitnum;
	    	if( pre[j] >= j ){
	    		continue;
	    	}//if
	    	else{
	    		res += j - pre[j];
	    		pre[j+1] += j - pre[j];
	    	}//else
	    	
	    }//for
        fprintf(fp2,"Case #%d: %d\n",i+1,res);		
	}
	
	
	fclose(fp1);
	fclose(fp2);
	return 0;
	
}
