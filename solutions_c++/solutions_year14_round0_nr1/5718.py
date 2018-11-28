//============================================================================
// Name        : gcj0a.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <stdio.h>
#include<cstring>
#include<stdlib.h>

int main() {
	int i,j,cas,row,temp,cnt,key,num2,num1;
	int in[20];
	freopen("A-small-attempt2.in","r",stdin);
	freopen("A-small-attempt2.out","w",stdout);
	scanf("%d",&cas);
	cnt=0;
	while(cas--){
		memset(in,0,sizeof(in));
		num2=0;
		num1=0;
		scanf("%d",&row);
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				scanf("%d",&temp);
				if(i==row)
					in[temp]+=1;
			}


		}

		scanf("%d",&row);
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
				scanf("%d",&temp);
				if(i==row)
					in[temp]+=1;


			}
		}
		for(i=1;i<=16;i++){
			if(in[i]==2){
				num2+=1;
				key=i;
			}
			if(in[i]==1)
				num1+=1;
		}
		if(num2==1)
			printf("Case #%d: %d\n",++cnt,key);
		if(num2>=2)
			printf("Case #%d: Bad magician!\n",++cnt);
		if(num1==8)
			printf("Case #%d: Volunteer cheated!\n",++cnt);

	}

	return 0;
}
