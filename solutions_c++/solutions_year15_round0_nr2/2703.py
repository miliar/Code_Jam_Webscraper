#include<stdio.h>
#include<cstdlib>
int main()
{
	freopen("inb.txt","r",stdin);
	freopen("outb.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int d;
	int p[1002];
	int x,y;
	int div,mnt;
	for(int ca=0;ca<t;ca++){
		scanf("%d",&d);
		for(int i=0;i<=1000;i++) p[i]=0;
		for(int i=0;i<d;i++){
			scanf("%d",&x);
			p[x]++;
		}
		mnt=10000000;
		for(int et=1;et<=1000;et++){
			div=0;
			for(int i=et+1;i<=1000;i++){
				div+=((i-1)/et)*p[i];
			}
			div+=et;
			if(div<mnt){
				mnt=div;
			}
		}
		printf("Case #%d: %d\n",ca+1,mnt);
	}
}
