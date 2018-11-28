#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

int solveSmall(const vector<int>& vi){
	vector<int> v = vi;
	vector<int> a(v.size());
	sort(v.begin(), v.end());
	int res = 10000000;
	vector<int> minV;
	do{
		bool valid = true;
		int maxPos = 0;
		for(int i=1;i<v.size();i++){
			if(v[maxPos] < v[i]) maxPos = i;
		}
		for(int i=0;i+1<=maxPos;i++){
			if(v[i] > v[i+1]) valid = false;
		}
		for(int i=maxPos;i+1<v.size();i++){
			if(v[i] < v[i+1]) valid = false;
		}
		if(!valid) continue;
		for(int i=0;i<v.size();i++){
			for(int j=0;j<vi.size();j++){
				if(v[i]==vi[j]) a[j] = i;
			}
		}
		int cnt = 0;
		for(int i=0;i<v.size();i++){
			for(int j=i+1;j<v.size();j++)
				if(a[i] > a[j]) cnt++;
		}
		if(cnt < res) minV = v;
		res = min(res, cnt);
	}while(next_permutation(v.begin(), v.end()));
	for(int i=0;i<vi.size();i++) cout << vi[i] << " "; cout << endl;
	for(int i=0;i<vi.size();i++) cout << minV[i] << " "; cout << endl;
	return res;
}

int solveLarge(const vector<int>& vi){
	vector<int> v = vi;
	vector<int> vp;
	for(int i=0;i<v.size();i++) vp.push_back(v[i]);
	sort(vp.begin(), vp.end());
	int l = 0, r = vi.size()-1;
	int res = 0;
	for(int i=0;i<vi.size();i++){
		int pos = -1;
		for(int j=l;j<=r;j++){
			if(v[j] == vp[i]){
				pos = j;
				break;
			}
		}
		if(pos-l < r-pos){
			res += pos-l;
			for(int j=pos;j-1>=l;j--) swap(v[j], v[j-1]);
			l++;
		} else {
			res += r-pos;
			for(int j=pos;j+1<=r;j++) swap(v[j], v[j+1]);
			r--;
		}
	}
	return res;
}

int main(){
	int T; cin >> T;
	for(int test=1;test<=T;test++){
		int N; cin >> N;
		vector<int> vi(N);
		for(int i=0;i<N;i++) cin >> vi[i];
		printf("Case #%d: %d\n", test, solveLarge(vi));
	}
}
