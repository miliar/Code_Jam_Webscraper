#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
void swap1(int s[],int i){
	for(int k=0;k<=i/2;k++){
		s[k]=(s[k]+1)%2;
		s[i-k]=(s[i-k]+1)%2;
		swap(s[k],s[i-k]);
	}
	if(i%2==0) s[i/2]=(s[i/2]+1)%2;
}

int main(){
	int C,cx=1;
	scanf("%d",&C);
	while(cx<=C){
		char str[110];
		int ans=0,n,s[110];
		scanf("%s",str);
		n=strlen(str);
		
		for(int i=0;i<n;i++){
			if(str[i]=='-') s[i]=0;
			else s[i]=1;
		}

		for(int i=n-1;i>=0;i--){
			if(s[i]==0){
				int z=0;
				bool check=false;
				while(s[z]==1) s[z++]=0,check=true;
				if(check) ans++;
				swap1(s,i);
		//		for(int m=0;m<n;m++)
		//			printf("%d ",s[m]);
		//		printf("\n");
				ans++;
			}
		}

		printf("Case #%d: %d\n",cx++,ans);
	}

	return 0;
}