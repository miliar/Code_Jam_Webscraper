#include<bits/stdc++.h>
using namespace std;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("out3","w",stdout);
	int n,cnt=0;
	char er[100000];
	scanf("%d",&n);
	for(int j=1 ; j<=n ; j++){
		char ch;
		scanf("%c%s",&ch,er);
		int res=0,cnt=0;
		for(int i=0 ; i<strlen(er) ; i++){
			if(er[i]=='+' && cnt==1){
				continue;
			}
			if(er[i]=='+' && !cnt){
				cnt=1;
				continue;
			}
			if(er[i]=='+' && cnt==2){
				cnt=1;
				res++;
				continue;
			}
			if(er[i]=='-' && cnt==2){
				continue;
			}
			if(er[i]=='-' && !cnt){
				cnt=2;
				continue;
			}
			if(er[i]=='-' && cnt==1){
				res++;
				cnt=2;
			}
		}
		if(er[strlen(er)-1]=='-'){
			res++;
		}
//		if(er[strlen(er)-1]=='+' && cnt==2){
//			res++;
//		}
		printf("Case #%d: %d\n",j,res);
	}
	return 0;
}
