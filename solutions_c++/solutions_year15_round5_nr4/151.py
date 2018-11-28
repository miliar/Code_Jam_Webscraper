
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>
#include <numeric>
#include <cassert>
#include <unordered_set>
#include <unordered_map>
#include <fstream>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)

ll binomial[62][62];

vector<ll> get_result2(vector<pair<ll,ll> > nums, bool & success){
//	for(auto it:nums)cout << "(" << it.first << " " << it.second << ")";
//	cout << endl;
	vector<ll> res;
	if(nums[0].first > 0 || nums[sz(nums)-1].first < 0){
		success = false;
		return res;
	}
	if(sz(nums) == 1 && nums[0] == mp((ll)0,(ll)1)){
		success = true;
		return res;
	}
	ll nv = nums[1].first - nums[0].first;
	success = false;

	FOR(num_neg,0,nums[1].second + 1){
		int num_pos = nums[1].second - num_neg;
		if(num_neg * -nv < nums[0].first)continue;
		if(num_pos * nv > nums[sz(nums)-1].first)continue;
		unordered_map<ll, ll> cur;
		FOR(i,0,num_pos+1)FOR(j,0,num_neg+1){
			cur[(i-j)*nv] += binomial[num_pos][i] * binomial[num_neg][j];
		}
		assert(cur[-num_neg * nv] == 1);
		cur.erase(-num_neg * nv);
		bool ok = true;
		unordered_map<ll, ll> done;
		vector<pair<ll, ll> > next_nums;
		FOR(i,0,sz(nums)){
			ll av = nums[i].second - done[nums[i].first];
			done.erase(nums[i].first);
			if(av < 0){
				ok = false;
				break;
			}
			if(av > 0){
				next_nums.push_back(mp(nums[i].first + num_neg * nv, av));
				for(auto it : cur){
					done[nums[i].first + num_neg * nv + it.first] += it.second * av;
				}
			}
		}
		if(!done.empty())ok = false;
		if(ok){
			vector<ll> tmp_res = get_result2(next_nums, ok);
			if(ok){
				FOR(i,0,num_neg)tmp_res.push_back(-nv);
				FOR(i,0,num_pos)tmp_res.push_back(nv);
				sort(all(tmp_res));
				if(success)res = min(res, tmp_res);
				else {
					success = true;
					res = tmp_res;
				}
			}
		}

	}
	return res;
}


vector<ll> get_result(vector<pair<ll,ll> > nums){
	int N = sz(nums);
	int Z = 0;
	while((1<<Z) != nums[0].second)++Z;
	FOR(i,0,N)nums[i].second /= (1<<Z);
	bool success = false;
	vector<ll> res = get_result2(nums, success);
	FOR(i,0,Z)res.push_back(0);
	sort(all(res));
	assert(success);
	return res;
}

void calc(){
	int P;
	cin >> P;
	vector<pair<ll, ll> > nums(P);
	FOR(i,0,P)cin >> nums[i].first;
	FOR(i,0,P)cin >> nums[i].second;
	sort(all(nums));
	vector<ll> res = get_result(nums);
	for(auto n: res)cout << " "  << n;
	cout << endl;
}

int main() {
	FOR(i,0,62){
		binomial[i][0] = binomial[i][i] = 1;
		FOR(j,1,i)binomial[i][j] = binomial[i-1][j] + binomial[i-1][j-1];
	}
	int TC;
	cin >> TC;
	FOR(tc,1,TC+1){
		cout << "Case #" << tc << ":";
		calc();
	}
	return 0;
}
