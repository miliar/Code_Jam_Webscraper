#include<bits/stdc++.h>
using namespace std;

char str[100009];

int main(){
	int t,xx,n,i,icnt,xi,k,pp,ans_offset,ans;
	scanf("%d",&t);
	for(xx=1;xx<=t;++xx){
		ans_offset=1; ans=0;
		scanf("%s",str);
		n=strlen(str);
		scanf("%d",&k);
		for(i=0;i<n;++i){
			if(str[i]=='+')
				continue;
			else{
				icnt=0;
				for(xi=i;xi<n;++xi){
                 	if(str[xi]=='-')
                 		++icnt;
                 	if(str[xi]=='+')
                 		break;
				}
				if(icnt>=k){
					++ans;
					i=i+k-1;
				}
				else{
					if(xi==n){
						ans_offset=0;
						i=n-1;
					}
					else{
                     	++ans;
                     	for(pp=i;pp<i+k&&pp<n;++pp){
                     		if(str[pp]=='+')
                     			str[pp]='-';
                     		else
                     			str[pp]='+';
                     	}
					}
				}

			}
		}
		printf("Case #%d: ",xx);
		if(ans_offset==0) printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
	}
	return 0;
}