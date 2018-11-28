#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

//YOLO
//loyolman
//pozdravujem citatelov dsl.sk

using namespace std;

int main() {
	int T;
	char up='^';
	char down='v';
	char left='<';
	char right='>';
	char no='.';
	
	cin>>T;
	for (int j=1;j<=T;j++) {
		int R,C;
		int changes=0;
		bool possible=true;
		cin>>R>>C;
		vector<vector<char> > array(R,vector<char> (C));
		
		for (int i=0;i<R;i++) for (int k=0;k<C;k++) cin>>array[i][k];
		
		for (int i=0;i<R;i++) for (int k=0;k<C;k++) {
			if (array[i][k]==no) continue;
			int sum=0;
			for (int o=0;o<C;o++) if (array[i][o]!=no) sum++;
			for (int o=0;o<R;o++) if (array[o][k]!=no) sum++;
			sum-=2;
			if (sum==0) possible=false;
			if (possible==false) break;
		}
		
		vector<int> done(C,0);
		for (int i=0;i<R;i++) for (int k=0;k<C;k++) {
			if (array[i][k]==no) continue;
			if (done[k]==0) {
				done[k]=1;
				if (array[i][k]==up) changes+=1;
			}
		}
		done.clear();done.resize(C,0);
		for (int i=R-1;i>=0;i--) for (int k=0;k<C;k++) {
			if (array[i][k]==no) continue;
			if (done[k]==0) {
				done[k]=1;
				if (array[i][k]==down) changes+=1;
			}
		}
		done.clear();done.resize(R,0);
		for (int i=0;i<R;i++) for (int k=0;k<C;k++) {
			if (array[i][k]==no) continue;
			if (done[i]==0) {
				done[i]=1;
				if (array[i][k]==left) changes+=1;
			}
		}
		done.clear();done.resize(R,0);
		for (int i=0;i<R;i++) for (int k=C-1;k>=0;k--) {
			if (array[i][k]==no) continue;
			if (done[i]==0) {
				done[i]=1;
				if (array[i][k]==right) changes+=1;
			}
		}
		
		cout<<"Case #"<<j<<": ";
		if (possible) cout<<changes<<endl;
		else cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}
