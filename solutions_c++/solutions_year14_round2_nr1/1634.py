#include<iostream>
#include<string>
#include<vector>

#include<algorithm>


using namespace std;


int main(){
	freopen("A-large.in", "r", stdin);
	freopen("output2.txt", "w", stdout);

	int tc;
	cin >> tc;

	for(int tt=1;tt<=tc;++tt){
		int n;
		bool omarLose = false;
		cin >> n;
		vector<string> vs(n,""), vs2;
		string tb;
		for(int j=0;j<n;++j) cin>>vs[j];
		tb = vs[0];
		tb.erase(unique(tb.begin(), tb.end()), tb.end());

		vs2 = vs;
		for(int j=0;j<n;++j) vs2[j].erase(unique(vs2[j].begin(), vs2[j].end()), vs2[j].end());
		for(int j=0;j<n;++j) if(vs2[j] != tb) omarLose = true;

		if(omarLose){ 
			cout << "Case #"<< tt <<": Fegla Won" << endl;
			continue;
		}
		vector< vector<int> > vvi (n,  vector<int>(tb.size(), 0));
		for(int j=0;j<n;++j){
			int tbk=0, vsk=0;
			while(vsk < vs[j].size() && tbk < tb.size()){
				if(tb[tbk] != vs[j][vsk]) {
					tbk++;
					continue;
				}
				vvi[j][tbk]++;
				vsk++;
			}
		}
		int ans = 0;
		for(int j=0;j<tb.size();++j){
			//vvi[?][j] ���� �ְ�/���� ���� ���Ѵ�.
			int vmin=101, vmax=0;
			for(int i=0;i<n;++i){
				vmin = min(vmin, vvi[i][j]);
				vmax = max(vmax, vvi[i][j]);
			}
			if(vmin == vmax) continue;
			int addto = 100000;
			for(int val=vmin; val<=vmax; ++val){// ���͵��� val �� ���⶧ �󸶳� ����� ����غ���
				int tmp = 0;
				for(int i=0;i<n;++i) tmp += std::abs(val - vvi[i][j] );
				addto = min(addto, tmp);
			}
			//����ؼ� �信 ���Ѵ�.
			ans += addto;
		}
		cout << "Case #"<<tt<<": " << ans<< endl;
	}

	return 0;
}