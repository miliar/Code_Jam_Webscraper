#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main (){
	int T,I;
	scanf("%d",&T);
	for(I=0;I<T;I++){
		char s[105];
		int a[105];
		scanf("%s",s);
		printf("Case #%d: ",I+1);
		int i,j,l=strlen(s),ans=0;
		for(i=0;i<l;i++){
			if(s[i]=='-')a[i]=0;
			else a[i]=1;
		}
		for(i=l-1;i>=0;i--){
			if(a[i]==0){
				break;
			}
		}
		l=i+1;
		while(l>0){
			int b[105];
			/*cout<<l<<endl;
			for(i=0;i<l;i++)printf("%d",a[i]);
			cout<<endl;*/
			if(a[0]==0){
				for(i=0;i<l;i++){
					b[i]=1-a[l-i-1];
				}
				for(i=0;i<l;i++){
					a[i]=b[i];
				}
			}
			else{
				for(i=l-1;i>=0;i--){
					if(a[i]==1){
						for(j=0;j<=i;j++){
							b[j]=1-a[i-j];
						}
						for(j=0;j<=i;j++){
							a[j]=b[j];
						}
					}
				}
			}
			ans++;
			for(i=l-1;i>=0;i--){
				if(a[i]==0)break;
			}
			l=i+1;
		}
		printf("%d\n",ans);
	}
	return 0;
}