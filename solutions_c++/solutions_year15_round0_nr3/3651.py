#include<iostream>
#include<stdlib.h>
using namespace std;

char xyz[100000];

int t,x,l,n,j,zz,i,flag,r;	
int a[4][4] = {
				{1, 2, 3, 4},
				{2,-1, 4,-3},
				{3,-4,-1, 2},
				{4, 3,-2,-1}
				};
int fetch(int x,int y);
int getsign(int a);		
int main(){
	
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	
	scanf("%d",&t);
	
	zz = 1;
	while(zz <=t){
		
		r=1;
		
		scanf("%d%d",&n,&l);
		scanf(" %s",xyz);
		
		flag = 1;
		for(j=0;j<l;j++)
			for(i=0;i<n;i++){
				if((r)==(flag+1)){
					flag++;
					r=1;
				}
				r = fetch(abs(r), xyz[i] - 'g')*getsign(r);
			}
		  
		if((r)==(flag+1)){
			flag++;
			r=1;
		}
		if(flag >3 && r == 1){
			printf("Case #%d: YES\n",zz);//YES
		}
		else{
			printf("Case #%d: NO\n",zz);//NO
		}
		zz++;
	}
}

int getsign(int a){
	if(a<0)
		return -1;
	return 1;
}

int fetch(int x,int y){
	return a[x-1][y-1];
}
