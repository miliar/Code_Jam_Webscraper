#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

typedef unsigned long long ll;

bool cmp(const pair<int, char> &l, const pair<int, char> &r) {
	return l.first>r.first;
}

int main() {
	int T; cin>>T;
	for (int testCase=1; testCase<=T; testCase++) {
		int N; cin>>N;
		vector<pair<int, char> > data(N); for (int i=0; i<N; i++) cin>>data[i].first, data[i].second='A'+i;
		
		cout<<"Case #"<<testCase<<": ";
		
		sort(data.begin(), data.end(), cmp);
		int k=0;
		while (k<N-1) {
			while (data[k].first>data[k+1].first) 
				for (int i=0; i<=k; i++) cout<<data[i].second<<" ", data[i].first--;
			k++;
		}
		
		while (data[0].first>0) {
			int i=0;
			data[0].first--;
			if (N%2==1) cout<<data[0].second<<" ", i++;
			for (; i<N; i+=2) cout<<data[i].second<<data[i+1].second<<" ";
		}
		cout<<endl;
	}
	return 0;
}
