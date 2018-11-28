#include<bits/stdc++.h>
#define rep(i,a,b) for(i=a;i<=b;i++)
using namespace std;
int main(){
	freopen("inp.txt","r",stdin);
	freopen("file.txt","w",stdout);
	int t;
	int idx = 1;
	cin >> t;
	int n,i,j;
	int trick[10][10];
	int trick1[10][10];
	
	while(t--){
		int cnt = 0;
		int r1,r2,val;
		cin >> r1;
		rep(i,1,4){
			rep(j,1,4){
				cin >> trick[i][j];
			}
		}
		cin >> r2;
		rep(i,1,4){
			rep(j,1,4){
				cin >> trick1[i][j];
			}
		}
		cnt = 0;
		val = 0;
		for(i=1;i<=4;i++){
			for(j=1;j<=4;j++){
			if(trick[r1][i] == trick1[r2][j]){
				//cout << trick[r1][i] << " " ;
				cnt++;
				if(cnt == 1){
				//	flag = 1;
					val = trick[r1][i];
				} 
			}
		}}//cout << cnt << "\n";
		if(cnt == 1){
			cout << "Case #" << idx << ":" << " " << val << "\n";
		}
		else if(cnt == 4 || cnt > 1){
			cout << "Case #"<< idx << ":" <<" "<<"Bad magician!"<<"\n";
		}
		else{
			cout << "Case #"<< idx << ":" <<" "<<"Volunteer cheated!"<<"\n";
		}
		idx ++;
		}
		return 0;
	}
