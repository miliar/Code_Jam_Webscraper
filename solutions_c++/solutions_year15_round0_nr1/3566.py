#include<bits/stdc++.h>
using namespace std;
int S[1010];
int main(){
	int standing,called,t,smax;
	char c;
	cin>>t;
	for(int k=1;k<=t;k++){
		cin>>smax;
		for(int i=0;i<=smax;i++){
			cin>>c;
			S[i]=c-'0';
		}
		standing=S[0];
		called=0;
		for(int i=1;i<=smax;i++){
			//printf("%d standing = %d ",i,standing);
			if(i>standing){
				called+=(i-standing);
				standing=i;
			}
			standing+=S[i];
			//printf("called = %d\n",called);
		}
		printf("Case #%d: %d\n",k,called);
	}
	return 0;
}
