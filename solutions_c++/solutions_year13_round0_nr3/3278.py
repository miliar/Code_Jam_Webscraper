#include <stdio.h>
#include <stdlib.h>
#include <string.h>

	char num[52];
int main(void)
{
	FILE *out;
	int ans[105];
	int nL=8,aL,sL,i,j,t;
	
	num[nL-1]=num[0]=1;
	if(nL%2){
		sL=(nL+1)/2;
		while(1){
			
			aL=nL+nL-1;
			for(i=0;i<nL;++i)
				ans[i]=num[i]*num[0];
			ans[aL]=0;
			for(i=1;i<nL;++i){
				for(j=i;j<nL;++j){
					ans[j]+=(num[i]*num[j-i]);
				}
			}
			for(i=1;i<nL;++i)
				ans[nL+i-1]=ans[nL-i-1];
			for(i=0;i<aL;++i){
				if(ans[i]>=10){
					ans[i+1]+=(ans[i]/10);
					ans[i]%=10;
				}
			}
			if(ans[aL])
				++aL;
			
			t=aL/2;
			for(i=0;i<t;++i)
				if(ans[i]!=ans[aL-i-1]){
					break;
				}
			if(i==t){
				out=fopen("num.txt","at");
				for(i=0;i<nL;++i)
					printf("%d",num[i]);
				printf(" ");
				for(i=aL-1;i>=0;--i)
					fprintf(out,"%d",ans[i]);
				fprintf(out,"\n");
				fclose(out);
			}			
			
			++num[sL-1];
			for(i=sL-1;i>0;--i)
				if(num[i]>9){
					num[i]=0;
					++num[i-1];
					num[nL-i-1]=num[i];
					num[nL-i]=num[i-1];
				}
			if(num[0]==10)
				break;
		}
	}
	else{
		sL=nL/2;
		while(1){
			
			aL=nL+nL-1;
			for(i=0;i<nL;++i)
				ans[i]=num[i]*num[0];
			ans[aL]=0;
			for(i=1;i<nL;++i){
				for(j=i;j<nL;++j){
					ans[j]+=(num[i]*num[j-i]);
				}
			}
			for(i=1;i<nL;++i)
				ans[nL+i-1]=ans[nL-i-1];
			for(i=0;i<aL;++i){
				if(ans[i]>=10){
					ans[i+1]+=(ans[i]/10);
					ans[i]%=10;
				}
			}
			if(ans[aL])
				++aL;
			
			t=aL/2;
			for(i=0;i<t;++i)
				if(ans[i]!=ans[aL-i-1]){
					break;
				}
			if(i==t){
				out=fopen("num.txt","at");
				for(i=0;i<nL;++i)
					printf("%d",num[i]);
				printf(" ");
				for(i=aL-1;i>=0;--i)
					fprintf(out,"%d",ans[i]);
				fprintf(out,"\n");
				fclose(out);
			}					
			
			num[sL]=++num[sL-1];
			for(i=sL-1;i>0;--i)
				if(num[i]>9){
					num[i]=0;
					++num[i-1];
					num[nL-i-1]=num[i];
					num[nL-i]=num[i-1];
				}
			if(num[0]==10)
				break;
		}
	}
	
	return 0;
}

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//		#define out stdout
//		#define in stdin

int main(void)
{
#ifndef in
	FILE *in;
	in=fopen("C-small-attempt0.in","rt");
	if(in==NULL){
		printf("\a");
		return -1;
	}
#endif
#ifndef out
	FILE *out;
	out=fopen("c.txt","wt");
	if(out==NULL){
		printf("\a");
		return -1;
	}
#endif
	int T,t,A,B,n,sum;
	fscanf(in,"%d",&T);
	for(t=1;t<=T;++t){
		fscanf(in,"%d %d",&A,&B);
		FILE *data=fopen("num.txt","rt");
		sum=0;
		while(fscanf(data,"%d",&n)!=EOF && n<=B){
			if(n>=A)
				++sum;
		}
		fprintf(out,"Case #%d: %d\n",t,sum);
	}
	
#ifndef in
	fclose(in);
#endif
#ifndef out
	fclose(out);
#endif
	return 0;
}

