#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int main(){
	freopen("p1.in","r",stdin);
	freopen("p1.out","w",stdout);
	int t;
	cin >> t; 
	int tc = 1;
	while(t--){
		int ans = -1;
		bool f = false;
		map<int,int> row;
		int arr[4][4];
		
		int ans1;
		cin >> ans1;
		ans1--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
				cin >> arr[i][j];
			if( i == ans1 )
				for(int j=0;j<4;j++)
					row[arr[i][j]]++;
		}
		int ans2;
		cin >> ans2;
		ans2 --;
		
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++)
				cin >> arr[i][j];
			if( i == ans2 )
				for(int j=0;j<4;j++){
					if( ans == -1 && row[arr[i][j]] == 1 ){
						ans  = arr[i][j];
					}else if( ans != -1 && row[arr[i][j]] == 1){
						f = 1;
					}
				}
		}
		
		cout << "Case #" << tc++ << ": ";
		if( ans == -1 ){
			cout << "Volunteer cheated!";
		}else if( f == 1 ){
			cout << "Bad magician!";
		}else{
			cout << ans;
		}
		cout << endl;
	}
}
