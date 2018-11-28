#include<stdio.h>
#include<string.h>
void change(char &a){
	if(a=='+'){
		a='-';
	}
	else{
		a='+';
	}
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("text.txt","w+",stdout);
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		char c[100];
		scanf("%s",c);
		int l=strlen(c);
		if(l==1){
			if(c[0]=='-'){
				printf("Case #%d: 1\n",i+1);
			}
			else{
				printf("Case #%d: 0\n",i+1);
			}
		}
		else{
			int time=0;
			char now=0;
			for(int j=1;j<l;j++){
				if(j!=l-1){
					if(c[j]!=c[now]){
						for(int k=0;k<=now;k++){
							change(c[k]);
						}
						time++;
					}
					now=j;
				}
				else{
					if(c[j]!=c[now]){
						for(int k=0;k<=now;k++){
							change(c[k]);
						}
						time++;
					}
					if(c[j]=='-'){
						time++;
					}
				}
			}
			printf("Case #%d: %d\n",i+1,time);
		}
	}
	fclose(stdin);
}
