#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	vector< vector<int> > v;
	vector<char>::iterator it;
	vector<int> maxr, maxc;
	int T,N,M,a;
	string G;
	cin>>T;
	string tmp;
	getline(cin, tmp);

	for(int i=1; i<=T; i++) {
		cout<<"Case #"<<i<<": ";
		cin>>N>>M;
		v.clear();maxr.clear();maxc.clear();
		maxr.resize(N);
		maxc.resize(M);
		for(int r=0; r<N; r++) {
			v.push_back(vector<int>());
			for(int c=0; c<M; c++) {
				cin>>a;
				v[r].push_back(a);
				if(a>maxr[r]){
					maxr[r] = a;
				}
				if(a>maxc[c]){
					maxc[c] = a;
				}
			}
		}

		bool bPossible=true;
		for(int r=0; r<v.size(); r++) {
			for(int c=0; c<v[r].size(); c++) {
				if(maxr[r]>v[r][c] && maxc[c]>v[r][c]){
					//cout<<endl<<r<<" "<<c<<" max:"<<maxr[r]<<" "<<maxr[c]<<" "<<v[r][c]<<endl;
					bPossible=false;
				}
			}
		}
		if(bPossible){
			cout<<"YES"<<endl;
		} else {
			cout<<"NO"<<endl;
		}
	}

	return 0;
}
