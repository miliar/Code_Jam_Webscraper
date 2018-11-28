#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main(){
	
	int n=0;
	
	freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
	scanf("%d",&n);
	for(int x=0;x<n;x++){
		int count=0;
		char tmp=0,last=0;
		char arry[115];
		scanf("%s",arry);
		int a =strlen(arry);
		for(int i=0;i<a;i++){
			if(arry[i]!=tmp){
				count++;
				tmp = arry[i];
			}
		}
		last = arry[a-1];
		
		if(last=='+')
			printf("Case #%d: %d\n",x+1,count-1);
		if(last=='-')
			printf("Case #%d: %d\n",x+1,count);
	}
	return 0;
	
}