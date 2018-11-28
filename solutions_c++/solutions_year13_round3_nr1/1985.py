#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
	int T,x,c=0;
	char s[105];
	cin >> T;
	while(T--){
		cin >> s >> x;
		int len = strlen(s);
		int res=0;
		for(int i=len-1;i>=0;i--){
			for(int j=0;j<=i-x+1;j++){
				int sum=0;
				int maxc=0;
				for(int k=j;k<=i;k++){
					if(s[k]=='a' || s[k]=='e' || s[k]=='i' || s[k]=='o' || s[k]=='u' ){
						if(sum>maxc) maxc = sum;
						sum=0;
					}
					else{
						sum++;
					}
				}
				if(sum>maxc) maxc=sum;
				if(maxc>=x) res++;
			}
		}
		printf("Case #%d: %d\n",++c,res);
	}
	return 0;
}
