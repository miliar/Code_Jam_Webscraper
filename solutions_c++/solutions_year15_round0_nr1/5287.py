#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("V:\\vikky_codder\\input.txt", "r", stdin);
	freopen("V:\\vikky_codder\\output.txt", "w", stdout);
	int tc;
	cin>>tc;
	for(int t=1;t<=tc;t++){
		int s;
		string str;
		cin>>s;
		cin>>str;
		int cur=0;
		int ans=0;
		for(int i=0;i<=s;i++){
			if(i>cur){
				ans+=(i-cur);
				cur+=(i-cur);
			}
			cur+=(str[i] - '0');
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
