#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main(){
	int t,sum,hasil,x,n;
	bool flag;
	int data[17];
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++){
		sum = hasil = 0;
		memset(data,0,sizeof(data));
		scanf("%d",&n);
		n--;
		for(int i=0;i<4;i++){
			if(i==n) flag = true;
			else flag = false;
			for(int j=0;j<4;j++){
				scanf("%d",&x);
				if(flag){
				
					data[x]++;
					if(data[x]==2)sum++,hasil = x;
				}
			}
		}
		scanf("%d",&n);
		n--;
		for(int i=0;i<4;i++){
			if(i==n) flag = true;
			else flag = false;
			for(int j=0;j<4;j++){
				scanf("%d",&x);
				if(flag){
					
					data[x]++;
					if(data[x]==2)sum++,hasil = x;
				}
			}
		}
		if(sum==1){
			printf("Case #%d: %d\n",tt,hasil);
		}
		else if(sum>1){
			printf("Case #%d: Bad magician!\n",tt);
		}
		else{
			printf("Case #%d: Volunteer cheated!\n",tt);
		}
	}
}