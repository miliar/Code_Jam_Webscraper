#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[]){

	freopen("C:\\Users\\Toshiba\\Desktop\\A-large.in","r",stdin);
	freopen("C:\\Users\\Toshiba\\Desktop\\output.txt","w",stdout);
	
	int t,tt;
	scanf("%d",&tt);
	string s;
	int freq[1005];

	for(t=0;t<tt;t++){
		int smax;
		scanf("%d",&smax);

		cin>>s;
		for(int i=0;i<smax+1;i++){
			freq[i]=s[i]-'0';
		}

		int standing=freq[0],ans=0;
		for(int i=1;i<smax+1;i++){
			if(standing<i){
				ans+=i-standing;
				standing+=freq[i]+i-standing;
			}
			else{
				standing+=freq[i];
			}
		}

		printf("Case #%d: %d\n",t+1,ans);

	}

	return 0;
}