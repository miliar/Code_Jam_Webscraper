#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int n;
	scanf("%d",&n);
	char s[200],tmp[200]; 
	for(int i=1; i<=n; ++i){
		int x;
		scanf("%s",s+1);
		printf("Case #%d: ", i);
		int l=strlen(s+1);
		int ans=0;
		for(int j=l;j>=1;--j) {
			if(s[j]=='-'){
				++ans;
				bool flip=0;
				if(s[1]=='+')flip=1; 
				for(int k=1;k<=j;++k)
					tmp[k]=s[j-k+1];
				for(int k=1;k<=j;++k)
					s[k] = (tmp[k]=='+') ? '-' : '+';
				if(flip)
					for(int k=1;k<=j;++k)
						s[k] = (s[k]=='+') ? '-' : '+';
			}
		}
		printf("%d\n",ans);
	}
	
	return 0;
}
