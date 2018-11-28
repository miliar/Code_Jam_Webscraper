#include <iostream>
int N[1000000];
int main (){
	int T,count,n,m,temp,temp2,k;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		scanf("%d",&N[i]);
		if(N[i]==0) printf("Case #%d: INSOMNIA\n",i+1);
		else{
			n=N[i];
			m=N[i];
			k=1;
			int check[10]={0};
			while(1){
				while(n!=0){
					check[n%10]=1;
					n=n/10;
				}
				count=0;
				for(int j=0;j<10;j++){
					if(check[j]==1){
						count++;
					}
				}
				if(count==10){
					printf("Case #%d: %d\n",i+1,temp2);
					break;
				} 
				temp=++k*m;
				n=temp;
				temp2=n;
			}
		}
	}
	return 0;
}