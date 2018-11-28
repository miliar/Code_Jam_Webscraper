#include <bits/stdc++.h>
using namespace std;



int main(){
//	freopen("B-large.in","r",stdin);
//	freopen("B-large.out","w",stdout);
	int t;
	cin>>t;
	int cas = 0;
	while(t--){
		cas++;
		
		int n,j;
		cin>>n>>j;
		
		int start = 1<<(n-2);
		int end = start*2;
		
		//cout<<start<<" "<<end<<endl;
		
		printf("Case #%d:\n",cas);
		
		for(int i=0;i<j;i++){
			stack<int> sta;
			int cur = start+i;
			while(cur){
				sta.push(cur&1);
				cur>>=1;
			}
			while(sta.size()){
				printf("%d",sta.top());
				sta.pop();
			}
			cout<<0;
			
			for(int k=2;k<=10;k++){
				cout<<" "<<k;
			}
			
			cout<<endl;
		}
		
		//printf("Case #%d: %d\n",cas,ans);
		
	}
	
	return 0;
}
