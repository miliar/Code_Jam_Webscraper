#include <iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
char c,arr[1001];

int main() {
	// your code goes here
	int t,cs,K,ans;
	cs=0;
	scanf("%d",&t);
	while(t--){
	    cs++;
	    c= getchar();
	    while(c!='+' && c!='-')
	    c= getchar();
	    int len=0;
	    while(c=='+' || c=='-'){
	        arr[len]=c;
	        c= getchar();
            len++;
	    }
	    scanf("%d",&K);
	    int j;
	    ans=0;
	    for(j=0;j<=(len-K);j++){
	        if(arr[j]=='+')
	        continue;
	        ans++;
	        for(int k=0;k<K;k++){
	            if(arr[j+k]=='-')
	            arr[j+k]='+';
	            else
	            arr[j+k]='-';
	        }
	    }
	    for(;j<len;j++){
	        if(arr[j]=='-'){
	            ans = -1;
	            break;
	        }
	    }
	    if(ans==-1)
	    printf("Case #%d: IMPOSSIBLE\n",cs);
	    else
	    printf("Case #%d: %d\n",cs,ans);
	}
	return 0;
}

