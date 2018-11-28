#include<cstdio>
#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;

#define reps(i,f,n) for(int i=f;i<int(n);i++)
#define rep(i,n) reps(i,0,n)

int main(){
	int T;
	cin>>T;
	
	reps(pp,1,T+1){
		int sum[22]={0};
		
		rep(k,2){
			int num;
			cin>>num;
			
			rep(i,4){
				rep(j,4){
					int a;
					cin>>a;
					
					if(i+1==num)sum[a]++;
				}
			}
		}
		
		vector<int> ans;
		reps(i,1,17){
			if(sum[i]==2)ans.push_back(i);
		}
		
		if(ans.empty()){
			printf("Case #%d: Volunteer cheated!\n",pp);
		}
		if(ans.size()==1){
			printf("Case #%d: %d\n",pp,ans[0]);
		}
		if(ans.size()>1){
			printf("Case #%d: Bad magician!\n",pp);
		}
	}
}