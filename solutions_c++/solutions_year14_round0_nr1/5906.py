#include <iostream>
using namespace std;

int main(){
	int n;
	cin >> n;
	for(int i=0;i<n;i++){
		int a;
		int map[4][4];
		int nums[4];
		int nums2[4];
		cin >> a;
		for(int x=0;x<4;x++){
			for(int y=0;y<4;y++){
				cin >> map[x][y];
			}
		}
		for(int x=0;x<4;x++){
			nums[x]=map[a-1][x];
		}
		cin >> a;
		for(int x=0;x<4;x++){
			for(int y=0;y<4;y++){
				cin >> map[x][y];
			}
		}
		for(int x=0;x<4;x++){
			nums2[x]=map[a-1][x];
		}
		int d=-1;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				if(nums[j]==nums2[k]){
					if(d==-1) {d=nums[j]; continue;}
					if(d==-2) {break;}
					d=-2;
					break;
				}
			}
		}
		if(d==-2) cout << "Case #" << i+1 << ": " << "Bad magician!";
		else if(d==-1) cout << "Case #" << i+1 << ": " << "Volunteer cheated!";
		else cout << "Case #" << i+1 << ": " << d;
		cout << '\n';
	}
	return 0;
}