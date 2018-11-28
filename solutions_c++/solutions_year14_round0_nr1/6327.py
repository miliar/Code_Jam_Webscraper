#include <iostream>
#include<stdio.h>

int arr1[4][4],arr2[4][4],t,n1,n2,p,v,dan1[4],dan2[4];
bool flag;
int check(int dan1[],int dan2[]){
	flag=false;v=0;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		  if(dan1[i]==dan2[j]){
  		    if(flag==false){
    		  	flag=true;
    		  	v=dan1[i];
    		  }
			else{
			  return 3;
				
			}	
  		  }
	}
	if(flag==false){
	return 0;
	}
	else{
		return 1;
	}
}
int main(){
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-practice.out", "w", stdout);
	scanf("%d",&t);
	for(int ii=0;ii<t;ii++){
		scanf("%d",&n1);
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				scanf("%d",&arr1[j][k]);
			}
		}
		for(int i=0;i<4;i++){
			dan1[i]=arr1[n1-1][i];
		}
		scanf("%d",&n2);
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				scanf("%d",&arr2[j][k]);
			}
		}
		for(int i=0;i<4;i++){
			dan2[i]=arr2[n2-1][i];
		}
		p=check(dan1,dan2);
		if(p==0){
			printf("Case #%d: Volunteer cheated!\n",ii+1);
		    continue;
		}else if(p==1){
			printf("Case #%d: %d\n",ii+1,v);
			continue;
		}else{
			printf("Case #%d: Bad magician!\n",ii+1);
		}
	}
		
}