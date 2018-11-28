#include<bits/stdc++.h>

using namespace std;

int solve(char s[],int n){
	int i,j,len,ans=0;
	len=strlen(s);
	for(i=0;i<len;i++){
		if(s[i]=='-'){
			if (len-i<n){
				return -1;
			};
			for(j=0;j<n;j++){
				if(s[i+j]=='-'){
					s[i+j]='+';
				} else s[i+j]='-';
			}
			ans++;
		}
	}
	return ans;
}

main(){
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int T,N,i,ans;
	char s[2000];
	cin>>T;
	for(i=0;i<T;i++){
		scanf("%s%d",&s,&N);
		cout<<"Case #"<<i+1<<": ";
		ans=solve(s,N);
		if (ans==-1){
			cout<<"IMPOSSIBLE"<<endl;
		} else{
			cout<<ans<<endl;
		}
	}
	return 0;
}
