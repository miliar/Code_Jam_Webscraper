#include<bits/stdc++.h>

using namespace std;

int main(){
	int t,i,j,k;
	string s;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		cin>>s;
		j=s.length()-1;
		int ans = 0;
		while(j>=0){
			while(j>=0 && s[j]=='+'){
				j--;
			}
			if(j>=0 && s[j]=='-'){
				ans++;
				while(j>=0 && s[j]=='-'){
					j--;
				}
				if(j!=-1){
					ans++;
				}
			}
			
			//for(k=0;k<j/2;k++){
			//	swap(s[k],s[j-k]);
			//}
		}
		printf("Case #%d: %d\n",i,ans);
	}
	
}
