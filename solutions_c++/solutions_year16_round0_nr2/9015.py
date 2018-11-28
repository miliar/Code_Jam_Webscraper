#include<stdio.h>
#include<string.h>
int main(){
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int test,cc=1,c=0,k;
	char in[101];
	scanf("%d",&test);
	
	while(test--){
		int i=0;
		
		scanf("%s",in);

	i= strlen(in);
		c=0,k=0;
		
		int l=i;
		for(int j=l-1;j>=0;j--){
			if(in[j]=='+')
				l--;
			else
				break;	
		}
	
		while(l>0){
		
			int kk=0;
			while(in[kk]=='+'){
				in[kk]='-';
				kk++;
				
			}
			if(kk>0)
			c++;
			k=0;
			char arr[101];
	
			
			for(int j=l-1;j>=0;j--){
				arr[k]=in[j];
				k++;
				
			}
		
			for(int j=0;j<l;j++){
				if(arr[j]=='+')
					in[j]='-';
				else
					in[j]='+';
			}
		
			c++;
			for(int j=l-1;j>=0;j--){
			if(in[j]=='+')
				l--;
			else
				break;	
			}	
		
		}
		
		printf("Case #%d: %d\n",cc,c);
		cc++;
	}
	return 0;
}
