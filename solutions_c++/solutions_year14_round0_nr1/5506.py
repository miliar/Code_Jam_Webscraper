#include<iostream>
#include<string>
#include<algorithm>
#include<vector>

using namespace std;

int main(){
        freopen("a.txt","r",stdin);	
	int T;cin>>T;
	for(int cn=1;cn<=T;cn++){
		int rn;
		int a[4][4];
		cin>>rn;
		for(int i=0;i<4;i++) for(int j=0;j<4;j++) cin>>a[i][j];
		
		int rn2;
		int b[4][4];
		cin>>rn2;
		for(int i=0;i<4;i++) for(int j=0;j<4;j++) cin>>b[i][j];
		int match = 0;
		int ans = 0;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(a[rn-1][i] == b[rn2-1][j]) { ans = a[rn-1][i];match++;}
			}
		}
		
		cout<<"Case #"<<cn<<": ";
		if(match == 0){
			cout<<"Volunteer cheated!\n";
		}else if(match == 1){
			cout<<ans<<endl;
		}else cout <<"Bad magician!\n";
	}
	
	return 0;
}
