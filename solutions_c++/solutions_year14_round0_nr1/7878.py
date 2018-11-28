#include<iostream>
using namespace std;
#include<stdio.h>

int main(){
	int t,r,ans,i,j,ans1,count;
	scanf("%d",&t);
	int inc=1;
	while(t--){
		int a[16];
		int f[20]={0};
		scanf("%d",&r);
		count=0;
		for(i=0 ; i<4 ; i++)
		for(j=0 ; j<4 ; j++)
		scanf("%d",&a[count++]);
		for(i=(r-1)*4 ; i<r*4 ; i++)
		f[a[i]]++;
		scanf("%d",&r);
		count=0;
		ans=0;
		for(i=0 ; i<4 ; i++)
		for(j=0 ; j<4 ; j++)
		scanf("%d",&a[count++]);
		for(i=(r-1)*4 ; i<r*4 ; i++){
			if(f[a[i]]==1){\
			ans++;
			ans1=a[i];
		}
		}
		if(ans==1)
		printf("Case #%d: %d\n",inc++,ans1);
		else if(ans==0)
		printf("Case #%d: Volunteer cheated!\n",inc++);
		else
		printf("Case #%d: Bad magician!\n",inc++);
	}
	return 0;
}
