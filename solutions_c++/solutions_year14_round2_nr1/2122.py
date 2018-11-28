#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<stdint.h>
#include<stdlib.h>
#include<climits>
#include<stdio.h>
#include<cmath>
#include<queue>
#include<vector>
#include<map>
using namespace std;
int main(){
    int t,n;
    char s[2][101];
    int temp[101][26] = {0};
    
    scanf("%d",&t);
    for(int te=1;te<=t;te++){
    	scanf("%d",&n);
    	
    	for(int j=0;j<n;j++){
    		scanf("%s",s[j]); 
    	}
    	
    	char *p = s[0];
    	char *q = s[1];
    	int count = 0;
    	bool f = true;
    	while(*p !='\0' || *q != '\0'){
    		
    		if(*p == *q) {
    			p++;q++;
    		}
    		if(*p != *q){
    			if(*p == *(p-1)){
    				++count;
    				p++;
    			}
    			else if(*q == *(q-1)){
    				++count;
    				q++;
    			}
    			else if(*(p-1) == *q){
    				q++;
    			}
    			else if(*(q-1) == *p){
    				p++;
    			}else{
    				f = false;
    				break;
    			}
    		}
    		
    		
    	}
    	if(f){
    		printf("Case #%d: %d\n",te,count);
    	}
    	else{
    		printf("Case #%d: Fegla Won\n",te);
    	}
    	
    	
    }
	return 0;
}

