#include <bits/stdc++.h>
using namespace std;

#define sd(x) scanf("%d",&x)
#define fr freopen("A-large.in","r",stdin)
#define fw freopen("Standing_Ovation_large.txt","w+",stdout)

int main(){
	fr;fw;
	int t,smax,ans,standing;
	sd(t);
	for(int x=1;x<=t;x++){
		sd(smax);
		standing=ans=0;
		char s[smax+1];
		scanf("%s",s);
		standing+=s[0]-'0';
		for(int i=1;i<=smax;i++){
			if(standing<i){
				ans+=i-standing;
				standing=i;				
			}
			standing+=s[i]-'0';
		}
		printf("Case #%d: %d\n",x,ans);
	}
	return 0;
}
