#include <iostream>
#include <fstream>
using namespace std;
int main(){
	ofstream ofs("output.txt");
	ifstream ifs("A-small-attempt0.in");
	int n; ifs >> n ;
	for(int i=1;i<=n;i++){
		int First,Second;
		ifs >> First;
		int a[4][4]; for(int j=0;j<4;j++) for(int k=0;k<4;k++) ifs >> a[j][k];
		ifs >> Second;
		int b[4][4]; for(int j=0;j<4;j++) for(int k=0;k<4;k++) ifs >> b[j][k];
		int cnt=0; int ans=0;
		for(int j=0;j<4;j++) for(int k=0;k<4;k++)
			if(a[First-1][j]==b[Second-1][k]) cnt++, ans=a[First-1][j];
		ofs << "Case #" << i << ": " ;
		if(cnt==0) ofs << "Volunteer cheated!" << '\n' ;
		else if(cnt>1) ofs << "Bad magician!" << '\n' ;
		else ofs << ans << '\n' ;
	}
}