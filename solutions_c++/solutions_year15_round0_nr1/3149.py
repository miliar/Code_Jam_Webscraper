#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

char s[2000];
int main(void){
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
		
		int n,a=0,ans=0;
		scanf("%d%s",&n,s);
		for(int i=0;i<=n;i++){
			if(a<i){ ans+=i-a; a=i; }
			a+=s[i]-'0';
		}
        
        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}

