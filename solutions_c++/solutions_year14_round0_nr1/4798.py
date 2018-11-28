#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	int N=0; cin>>N;
	for(int o=0; o<N;++o){
		vector<vector<int>> c (4,vector<int>(4,0));
		int v=0; cin>>v; --v;
		for(int i=0;i<4;++i)
			cin>>c[i][0]>>c[i][1]>>c[i][2]>>c[i][3];
		vector<int> b=c[v];
		int v1=0; cin>>v1; --v1;
		for(int i=0;i<4;++i)
			cin>>c[i][0]>>c[i][1]>>c[i][2]>>c[i][3];
		int k=0, a=0;
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				if(b[i]==c[v1][j])++k,a=b[i];
		cout<<"Case #"<<o+1<<": ";
		if(k==0) cout<<"Volunteer cheated!"<<endl;
		if(k==1) cout<<a<<endl;
		if(k>1) cout<<"Bad magician!"<<endl;
	}
	return 0;
}