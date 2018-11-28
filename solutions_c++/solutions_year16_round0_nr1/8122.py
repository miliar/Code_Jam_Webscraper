#include<stdio.h>
#include<string>
#include<string.h>
#include<math.h>
#include<stdlib.h>
int checkdigit(int a){
	int check=0;
	while(a!=0){
		a=a/10;
		check++;
	}
	return check;
}
char* changents(int a){
	int l=checkdigit(a);
	char *c;
	c=(char *)malloc(l*sizeof(char));
	for(int i=0;i<l;i++){
		c[i]=a/(int)pow(10,l-i)+48;
		a-=(a/(int)pow(10,l-i))*pow(10,l-i);
	}
	return c;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("text.txt","w+",stdout);
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		int num;
		int a[10]={0};
		int check=0;
		int final;
		scanf("%d",&num);
		if(num==0){
			printf("Case #%d: INSOMNIA\n",i+1);
		}
		else{
			int time=0;
			while(check!=10){
				int use=num*(time+1);
				int b=use;
				int l=checkdigit(b);
				char *c;
				c=(char *)malloc(l*sizeof(char));
				for(int i=0;i<l;i++){
					c[i]=b/(int)pow(10,l-i-1)+48;
					b-=(b/(int)pow(10,l-i-1))*pow(10,l-i-1);
				}
				for(int i=0;i<l;i++){
					if(a[c[i]-48]==0){
						a[c[i]-48]=1;
						check++;
					}
				}
				if(check==10){
					final=use;
				}
				time++;
			}
			printf("Case #%d: %d\n",i+1,final);
		}
	}
	fclose(stdout);
}
