#include<iostream>
#include<cstring>
#include<algorithm>
char s[2000];
using namespace std;
int main(){
    int T;
    scanf("%d",&T);
    for(int j=1;j<=T;j++){
    	int n;
    	scanf("%d",&n);
    	scanf("%s",s);
    	int ans=0;
    	int sum=0;
    	for(int i=0;i<strlen(s);i++){
    		ans=max(ans,i-sum);
		sum+=s[i]-'0';
    	}
    	printf("Case #%d: %d\n",j,ans);
    }
}
