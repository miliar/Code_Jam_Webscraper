#include<bits/stdc++.h>
#define M 101
#define SWAP(a,b,t) ((t=a),(a=b),(b=t))
using namespace std;
int findmin(char s[],int n){
	int i,j,k,cnt=0;
	if(s[n-1]=='-')
		cnt++;
	char prev=s[0];
	for(i=1;i<n;i++){
		if(s[i]==prev)
			continue;
		else{
			cnt++;
			prev=s[i];
		}
	}	
	return cnt;
}
int main(){
	freopen("B-large.in","r",stdin);
    freopen("B-large-output.out","w",stdout);
	
	int t,i,j,k,n,ans;
	char s[M];
	cin>>t;
	for(i=1;i<=t;i++){
		cin>>s;
		n=strlen(s);
		ans=findmin(s,n);
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}
