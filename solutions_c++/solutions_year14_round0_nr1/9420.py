#include<cstdio>
int main(){
	int T,z,row1,row2,a[20],b[20],i,count,j,tmp;
	scanf("%d",&T);
	for(z=1;z<=T;z++){
		count=0;
		tmp=0;
		scanf("%d",&row1);
		for(i=0;i<16;i++) scanf("%d",&(a[i]));
		scanf("%d",&row2);
		for(i=0;i<16;i++) scanf("%d",&(b[i]));
		for(i=4*row1-4;i<=4*row1-1;i++){
			for(j=4*row2-4;j<=4*row2-1;j++){
				if(a[i]==b[j]){
					count++;
					tmp=a[i];
				}
			}
		}
		if(count==1) printf("Case #%d: %d\n",z,tmp);
		else if(count>1) printf("Case #%d: Bad magician!\n",z);
		else if(count==0) printf("Case #%d: Volunteer cheated!\n",z);
	}
	return 0;
}

