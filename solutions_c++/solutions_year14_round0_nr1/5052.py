#include<stdio.h>
#include<cstring>
#include<cmath>
#include<iostream>

using namespace std;
int a[5],b[5],c[5];

int f_cmp(){
	int cnt=0;
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(a[i]==b[j]){
				c[cnt++]=a[i];
				break;
			}
		}
	}
	return cnt;
}
int main(){
	int r1,r2,t,t1,t2,t3,t4,n;
	cin >> t;
	n=t;
	while(t--){
		cin >> r1;
		for(int i=0;i<4;i++){
			scanf("%d%d%d%d",&t1,&t2,&t3,&t4);
			if(i==r1-1){
				a[0]=t1;a[1]=t2;
				a[2]=t3;a[3]=t4;
			}
		}
		cin >> r2;
		for(int i=0;i<4;i++){
			scanf("%d%d%d%d",&t1,&t2,&t3,&t4);
			if(i==r2-1){
				b[0]=t1;b[1]=t2;
				b[2]=t3;b[3]=t4;
			}
		}

		int cnt=f_cmp();
		if(cnt==1){
			printf("Case #%d: %d\n",n-t,c[0]);
		}
		else if(cnt==0){
			printf("Case #%d: Volunteer cheated!\n",n-t);
		}
		else printf("Case #%d: Bad magician!\n",n-t);
	}
	return 0;
}

