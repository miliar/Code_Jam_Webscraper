#include <iostream>
#include <string>
#include <vector>
#include <bitset>

using namespace std;

#define int long long


int mypow(const int& a, const int& n){
	int res = 1;
	for(int i=0;i<n;i++) res *= a;
	return res;
}

vector<int> ini(const int& N){
	vector<int> res;
	vector<int> is_pnum(N, 1);

	is_pnum[0] = 9;
	is_pnum[1] = 9;
	for(int i=2;i<N;i++){
		for(int j=2*i;j<N;j+=i){
			is_pnum[j] = 0;
		}
	}
	for(int i=0;i<N;i++) if(!is_pnum[i]) res.push_back(i);

	return res;
}

vector<int> ini2(const vector<int>& a, const int& N){
	vector<int> res;
	for(auto& i : a){
		if(!(i & 1)) continue;
		if(!(i & 1<<N-1)) continue;
		res.push_back(i);
	}
	return res;
}

void solve(){
	// N=16, J=50
	// N=32, J=500
	int N, J;
	cin>> N>> J;

	vector<int> not_pnums = ini(mypow(2, N));
	//cerr<< "not_pnums"; for(auto i: not_pnums) cerr<< " "<< i; cerr<< endl;

	vector<int> may_jcs = ini2(not_pnums, N);
	//cerr<< "may_jcs"; for(auto i: may_jcs) cerr<< " "<< i; cerr<< endl;

	int cnt = 0;
	for(auto& num : may_jcs){
		if(cnt == J) break;

		vector<int> ipted_nums;
		for(int j=2;j<=10;j++){
			int ipted_num = 0;
			int jj=1;
			for(int k=0;k<N;k++){
				if(num & 1<<k) ipted_num += jj;
				jj *= j;
			}
			ipted_nums.push_back(ipted_num);
		}

		vector<int> ntdivs;
		bool is_jc = true;
		for(auto& i : ipted_nums){
			bool has_ntdiv = false;
			for(int j=2;j*j<=i;j++){
				if(i % j == 0){
					ntdivs.push_back(j);
					has_ntdiv = true;
					break;
				}
			}
			if(!has_ntdiv){
				is_jc = false;
				break;
			}
		}
		if(!is_jc) continue;

		int jc = num;
		cout<< bitset<16>(jc).to_string().substr(16-N);
		for(auto& i : ntdivs) cout<< " "<< i;
		cout<< endl;

		cnt++;
	}

	return;
}

signed main(){
	int n;
	cin>> n;
	for(int i=0;i<n;i++){
		cout<< "Case #"<< i+1 << ": "<< endl;
		solve();
	}
	return 0;
}
