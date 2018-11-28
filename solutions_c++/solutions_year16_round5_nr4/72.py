#include <bits/stdc++.h>


using namespace std;

char good[111][111];

char bad[111];

int main(){
	freopen("D-small-attempt1.in","r",stdin);
    freopen("D-small-attempt1.out","w",stdout);
    
	int t;
	cin>>t;
	
	int cas = 0;
	while(t--){
		cas++;
		
		int n,l;
		cin>>n>>l;
		
		
		int MAX = 0;
		for(int i=1;i<=n;i++){
			scanf("%s",good[i]);
			int cnt = 0;
			for(int j=0;j<l;j++){
				if(good[i][j]=='1'){
					cnt++;
				}
			}
			MAX = max(MAX,cnt);
		}
		
		scanf("%s",bad);
		
		printf("Case #%d: ",cas);
		
		if(MAX == l){
			cout<<"IMPOSSIBLE"<<endl;
		}else{
			
			string str = "";
			
			for(int i=0;i<30;i++){
				str+="10";
			} 
			
			str+="?";
			for(int i=0;i<30;i++){
				str+="10";
			} 
			
			string qq = "0";
			for(int i=0;i<l-1;i++){
				qq+="?";
			}
			
			cout<<qq<<" "<<str<<endl;
			
		}
		
		
	}
	
	return 0;
}
