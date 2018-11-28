#include <bits/stdc++.h>
using namespace std;
int main(int argc, char const *argv[])
{
	int t,k=1;
	scanf("%d",&t);
	while(k<=t){
		string s;
		cin>>s;
		int n = s.length();
		bool all_plus = true, all_minus = true;
		for(int i=0;i<n;i++){
			if(s[i]=='-'){
				all_plus=false;
			}
			else if(s[i]=='+'){
				all_minus=false;
			}
		}
		if(all_minus){
			printf("Case #%d: 1\n",k);
		}
		else if(all_plus){
			printf("Case #%d: 0\n",k);
		}
		else{
			string res = "";
			res += s[0];
			for(int i=1;i<n;i++){
				if(s[i]!=s[i-1]){
					res += s[i];
				}
			}
			int len = res.length();
			int ans = 0;
			if(res[len-1]=='+'){
				ans = len-1;
			}
			else{
				ans = len;
			}
			printf("Case #%d: %d\n",k,ans);
		}
		k++;
	}
	return 0;
}