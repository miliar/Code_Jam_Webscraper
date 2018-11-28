#include <iostream>
using namespace std;

int grid[5][5];

void getGrid(){
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			cin >> grid[i][j];
		}
	}
}

int play(){
	int line;
	int num[20]={0};
	int tot=0;	
	cin >> line;
	
	getGrid();
	
	for(int i=0;i<4;i++) num[grid[line-1][i]]++;
	
	cin >> line;
	
	getGrid();
	
	for(int i=0;i<4;i++) num[grid[line-1][i]]++;
	
	int last=0;
	
	for(int i=0;i<20;i++){
		if(num[i]==2){
			tot++;
			last=i;
		}
	}
	
	if(tot==1) return last;
	else if(tot==0) return -2;
	else return -1;
}

int main() {
	int t;
	cin >> t;
	
	for(int g=1;g<=t;g++){
		int ans=play();
		cout << "Case #" << g << ": ";
		if(ans==-1) cout << "Bad magician!" << endl;
		else if(ans==-2) cout << "Volunteer cheated!" << endl;
		else cout << ans << endl;
	}
	
	return 0;
}