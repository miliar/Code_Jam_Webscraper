#include<stdio.h>

using namespace std;

int main(){
	int tc,t=1;
	int n;
	int len,temp,needed;
	int total;
	char in[1002];
	scanf("%d",&tc);
	while(t<=tc){
		scanf("%d",&n);
		scanf("%s",in);
		//printf("%s\n",in);
		len=0;
		total=0;
		needed=0;
		while(len<=n){
		
			temp=in[len]-48;
			
			if(total>=len)
				total+=temp;
			else{
				needed+=1;
				total+=(temp+1);
			}
				
			
			len++;
		}
		//printf("%d\n",total);
		printf("Case #%d: %d\n",t,needed);
		t++;
	}
}
