#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

int main() {
	ifstream inp("A-small-attempt0.in");
	cin.rdbuf(inp.rdbuf());
	ofstream out("output.txt");
	cout.rdbuf(out.rdbuf());
	int T; cin>>T;
	for(int t=1; t<=T; t++) {
		vector<int> res(17);
		for(int i=0; i<2; i++) {
			int a; cin>>a; a--;
			int ar[4][4];
			for(int i=0; i<4; i++)
				for(int j=0; j<4; j++)
					cin>>ar[i][j];
			for(int i=0; i<4; i++)
				res[ar[a][i]]++;
		}
		cout<<"Case #"<<t<<": ";
		int c = count(res.begin(), res.end(), 2);
		if (c==1) cout<<find(res.begin(), res.end(), 2)-res.begin()<<endl;
		else if (c>1) cout<<"Bad magician!"<<endl;
		else cout<<"Volunteer cheated!"<<endl;
	}
	return 0;
}
