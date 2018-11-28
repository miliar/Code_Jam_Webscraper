#include <iostream>
#include<cstdio>
#include<cstring>
using namespace std;

int main() {
	int t,T,arrangement[18],count,ans1,ans2,row1[5],row2[5],num;
	int i,j;
	scanf("%d",&T);
	for(t=1;t<=T;++t){
		scanf("%d",&ans1);
		for(i=0;i<16;++i)
			scanf("%d",&arrangement[i]);
		for(i=0;i<4;++i)
			row1[i]=arrangement[4*(ans1-1)+i];

		scanf("%d",&ans2);
		for(i=0;i<16;++i)
			scanf("%d",&arrangement[i]);
		for(i=0;i<4;++i)
			row2[i]=arrangement[4*(ans2-1)+i];

		count=0;
		for(i=0;i<4;++i)
			for(j=0;j<4;++j){
				if(row1[i]==row2[j])
					++count,num=row1[i];
			}
		printf("Case #%d: ",t);
		if(count==0)
			printf("Volunteer cheated!\n");
		else if(count==1)
			printf("%d\n",num);
		else
			printf("Bad magician!\n");
	}
	return 0;
}
