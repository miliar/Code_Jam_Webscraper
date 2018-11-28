#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(){
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,cc=1,c=0,k;
	char in[101];
	scanf("%d",&t);
	//printf("%d",t);
	while(t--){
		char ch,ch1;
		int i=0;
		//fflush(stdin);
		//ch1=getchar();
		/*ch=getchar();
		while(ch!='\n'){
			in[i]=ch;
			i++;
			ch=getchar();
			fflush(stdin);
		}*/
		scanf("%s",in);
	//	printf("%d %s\n",i,in);
	i= strlen(in);
		c=0,k=0;
		
		int l=i;
		for(int j=l-1;j>=0;j--){
			if(in[j]=='+')
				l--;
			else
				break;	
		}
	//	
		while(l>0){
		//	printf("in=%s\n",in);
			int kk=0;
			while(in[kk]=='+'){
				in[kk]='-';
				kk++;
				
			}
			if(kk>0)
			c++;
			k=0;
			char arr[101];
		//	printf("l=%d \n",l);
			
			for(int j=l-1;j>=0;j--){
				arr[k]=in[j];
				k++;
				//printf("arrk =%c inj= %c\n",arr[k],in[j]);
			}
		//	printf("rev =%s and in=%s \n",arr,in);
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
		//	printf("new l=%d\n",l);
			//printf("after swap =%s \n",in);
		}
		
		printf("Case #%d: %d\n",cc,c);
		cc++;
	}
	return 0;
}
