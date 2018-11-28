#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main(){
	long long int a=0;
	int n=0;
	freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
	scanf("%d",&n);
	for(int x=0;x<n;x++){
		scanf("%lld",&a);
		long long int other=0,now=0,last=0;
		int arry[10]; 
		for(int i=0;i<10;i++)
			arry[i]=0;
		int dex=0;
		for(int i=1;i<100;i++){
			other = a*i;
			dex=0;
			for(int j=0;j<10;j++){			
					now=other%10;
					other=other/10;
					arry[now]=1;
				if(other==0){break;}
				
			}
			for(int j=0;j<10;j++){
				if(arry[j]==0){dex=1;}
				//printf("%d ",arry[j]);
			}
				//printf("%d\n",i);
			if(dex==0){
				last=a*i;
				//printf("%d\n",i);
				break;
			}
		}
		
		if(dex==0)
			printf("Case #%d: %lld\n",x+1,last);
		if(dex==1)
			printf("Case #%d: INSOMNIA\n",x+1);
	}
	return 0;
	
}