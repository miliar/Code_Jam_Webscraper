#include<cstdio>


int main(){
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		int hash[10]={0},inputJra;
		scanf("%d",&inputJra);
		if(inputJra==0){
			printf("Case #%d: INSOMNIA\n",i+1);
		}else
		for(int j=inputJra;true;j+=inputJra){
			//printf("%d\n",j);
			int tmp=j;
			while(tmp>0){
				hash[tmp%10]=1;
				tmp/=10;
			}
			bool b =true;
			for(int k=0;k<10;k++){
				if(hash[k]==0){
					b=false;
					break;
				}
			}
			if(b){
				printf("Case #%d: %d\n",i+1,j);
				break;
			}
		}
	}
}
