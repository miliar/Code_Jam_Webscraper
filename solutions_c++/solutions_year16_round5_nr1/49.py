#include <bits/stdc++.h>
using namespace std;
int Test,ans,last,len;
char s[20010],sta[20010];
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&Test);
	for (int tt=1;tt<=Test;tt++){
		printf("Case #%d: ",tt);
		scanf("%s",s);
		len=strlen(s);
		last=0;
		ans=0;
		for (int i=0;i<len;i++){
			if (last&&s[i]==sta[last]){
				sta[last--]=0;
				ans+=10;
			}else sta[++last]=s[i];
		}
		printf("%d\n",ans+last/2*5);
	}
}