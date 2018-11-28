#include<iostream>
#include<string>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<algorithm>
#define all(x) x.begin(),x.end()
#define tr(container,iterator) for(typeof(container.begin()) iterator=container.begin();iterator!=container.end();++iterator)

using namespace std;
long long i,j;

long solve(vector<int>& v){
	long audience = 0;
	long shy_l = 0;
	long ans = 0;
	tr(v,it){
		//cout << *it << " " << shy_l << ":" << audience << ';' << ans << endl;
		if(shy_l > audience and *it > 0){
			ans += (shy_l-audience);
			audience += (shy_l-audience);
		}
		audience += *it;
		++shy_l;
	}
	return ans;
}

int main(){
	int t,tc=0;
	int s_max;
	string str;
	vector<int> v;
	str.reserve(1005);
	cin >> t;
	while(t--){
		cout << "Case #" << ++tc << ": ";
		cin >> s_max >> str;
		v.clear();
		for(i=0;i<s_max+1;++i){
			v.push_back(str[i]-48);
		}
		cout << solve(v);
		cout << endl;
	}
	return 0;
}