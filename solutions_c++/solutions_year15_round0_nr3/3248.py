#include<stdio.h>
#define I 2
#define J 3
#define K 4
#define POS 0
#define NEG 1
int main(){
	int t,k=0,flag,sign,cur;
	long long int l,x,i,j;
	char str[100005];
	char mult[5][5];
	mult[1][1]=1;mult[1][I]=I;mult[1][J]=J;mult[1][K]=K;
	mult[I][1]=I;mult[I][I]=-1;mult[I][J]=K;mult[I][K]=-J;
	mult[J][1]=J;mult[J][I]=-K;mult[J][J]=-1;mult[J][K]=I;
	mult[K][1]=K;mult[K][I]=J;mult[K][J]=-I;mult[K][K]=-1;
	
	/*
	for(i=1;i<5;i++){
		for(j=1;j<5;j++)
			printf("%d ",mult[i][j]);
		printf("\n");
	}
	*/
	
	
	scanf("%d",&t);
	
	while(k<t){
		flag=1;
		
		scanf("%d %d",&l,&x);
		scanf("%s",str);
		//printf("Hello k=%d\n",k);
		for(i=0;i<l;i++){
			for(j=1;j<x;j++){
				str[i+l*j]=str[i];
			}
		}
		
		str[i+(l*x)]='\0';
		
		//printf("%s\n",str);
		/*
		if(k==60){
			printf("%d %d\n",l,x);
			printf("%s",str);
			break;
		}
		*/
		
		if((l*x)<3){
			printf("Case #%d: NO\n",++k);
			continue;
		}
		
		
		sign=POS;
		cur=1;
		flag=0;
		for(i=0;i<(l*x);i++){
			cur=mult[cur][str[i]-103];
			if(cur<0){
				if(sign==NEG){
					cur*=-1;
					sign=POS;
				}
				else{
					cur*=-1;
					sign=NEG;
				}
			}
			
			if(cur==I){
				if(sign==POS){
					flag=1;
					i++;
					break;		
				}
			}
		}
		
		if(flag==1){
			cur=1;
			flag=0;
			for(;i<(l*x);i++){
				cur=mult[cur][str[i]-103];
				if(cur<0){
					if(sign==NEG){
						cur*=-1;
						sign=POS;
					}
					else{
						cur*=-1;
						sign=NEG;
					}
				}
				
				if(cur==J){
					if(sign==POS){
						flag=1;
						i++;
						break;		
					}
				}
			}
		}
		else{
			printf("Case #%d: NO\n",++k);
			continue;
		}
		
		if(flag==1){
			cur=1;
			flag=0;
			for(;i<(l*x);i++){
				cur=mult[cur][str[i]-103];
				if(cur<0){
					if(sign==NEG){
						cur*=-1;
						sign=POS;
					}
					else{
						cur*=-1;
						sign=NEG;
					}
				}
			}
			
			if(cur==K){
				if(sign==POS){
					printf("Case #%d: YES\n",++k);
					continue;		
				}
			}
			
		}
		else{
			printf("Case #%d: NO\n",++k);
			continue;
		}	
		
		printf("Case #%d: NO\n",++k);
	}
	
	return 0;
}
