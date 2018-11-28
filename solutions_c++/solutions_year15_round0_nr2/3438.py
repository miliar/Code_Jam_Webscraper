#include <bits/stdc++.h>
using namespace std;

#define Read freopen("in.in","rt",stdin);
#define Print freopen("out.out","wt",stdout);
vector<int>input;
int main(){
	Read
	Print
	int t;
	int n;
	int nt = 0;
	cin>>t;
	while(t--){
		nt++;
		cin>>n;
		input.resize(n);
		int mx = 0;
		for(int i=0;i<n;i++){
			cin>>input[i];
			mx = max(mx , input[i]);
		}
		int ans = mx;
		for(int final = 1 ; final <= 1000 ; final++){

			int proper_answer = 0;

			for(int i=0;i<n;i++){
				proper_answer += (input[i]+final-1) / final -1 ;
			}
			ans = min(ans , proper_answer + final);
		}
		printf("Case #%d: %d\n" ,nt,ans);
	}

}
