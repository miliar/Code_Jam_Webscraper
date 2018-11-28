#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main(){
	int test; scanf("%d",&test);
	for(int t=1;t<=test;t++){
		printf("Case #%d: ",t);
		int n; scanf("%d",&n);
		int a[n];
		int num=n;
		for(int i=0;i<n;i++) scanf("%d",&a[i]);
		while(true){
			if(num==0) break;
			int max=0,smax=0,pos,poss,c=2;
			for(int i=0;i<n;i++){
				if(max<a[i]){
					smax=max;
					max=a[i];
					poss=pos;
					pos=i;
				}
				else if(smax<a[i]){
					smax=a[i];
					poss=i;
				}
			}
			if(max>1 && smax>1) {
				a[pos]--;
				a[poss]--;
				printf("%c%c ",'A'+pos,'A'+poss);
				continue;
			}
            else if(max>1 && smax<=1){
            	a[pos]-=2;
            	if(a[pos]==0) num--;
            	printf("%c%c ",'A'+pos,'A'+pos);
            }
            else{
            	if(num>3){
            		for(int i=0;i<n;i++) if(a[i]==1 && c>0) {
            			a[i]--;
            			num--;
            			c--;
		                printf("%c",'A'+i);
            		}
            		printf(" ");
            	}
            	else if(num==3) {
            		c=1;
            		for(int i=0;i<n;i++) if(a[i]==1 && c>0){
            			a[i]--;
            			num--;
            			c--;
            			printf("%c ",'A'+i);
            		} 
            	}
            	else{
            		for(int i=0;i<n;i++) if(a[i]==1) printf("%c",'A'+i);
            		num=0;
            	}
            }
		}
		printf("\n");
	}
	return 0;
}