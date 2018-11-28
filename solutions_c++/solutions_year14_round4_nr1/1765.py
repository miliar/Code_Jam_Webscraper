#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

vector<int> S;

int main() {

	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int T, X, N, Si;

	cin>>T;
	for(int t=1 ; t<=T ; t++) {
		int ans=0;

		cin>>N>>X;
		for(int i=0 ; i<N ; i++) {
			cin>>Si;
			S.push_back(Si);
		}

		sort(S.begin(), S.end());
		while(!S.empty()) {
			int num1 = S[(int)S.size()-1], i;
			if(S.size()==1) i=-1; 
			else for(i=(int)S.size()-2 ; i>=0 && num1+S[i]>X ; i--);

			S.erase(S.begin()+S.size()-1);
			if(i>=0) S.erase(S.begin()+i);
			ans++;
		}

		cout<<"Case #"<<t<<": "<<ans<<endl;
	}

	return 0;
}