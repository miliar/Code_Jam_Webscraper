#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

bool pal(long long a){
	vector<int> v;
	while (a > 0){
		v.push_back(a % 10);
		a /= 10;
	}
	for (int i = 0, j = v.size() - 1; i <= j; i++, j--)
		if (v[i] != v[j])
			return false;
	return true;
}

int binsearch(vector<pair<long long, int> > v, long long a){
	long long res = 0;
	int l = 0, r = v.size() - 1;
	while (l <= r){
		int mid = (l + r) >> 1;
		if (v[mid].first < a){
			res = v[mid].second;
			l = mid + 1;
		}
		else
			r = mid - 1;
	}
	return res;
}

long long prec[41] = {0, 1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004, 100000020000001};

void build(){
	vector<pair<long long, int> > v;
	long long mod = 10000000;
	int cnt = 0;
	for (long long s = 1; s <= mod; s++){
		if (pal(s) && pal(s * s)){
			cnt++;
			v.push_back(make_pair(s * s, cnt));
		}
	}	
	v.push_back(make_pair((mod + 1) * (mod + 1), cnt + 1));
		
	cout<<"int v["<<cnt<<"] = {0";
	for (int i = 0; i < v.size(); i++)
		cout<<", "<<v[i].first;
	cout<<"};"<<endl;

}

int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);

	int T;
	cin>>T;
	
	vector<pair<long long, int> > v;
	for (int i = 0; i < 41; i++)
		v.push_back(make_pair(prec[i], i));

	for (int t = 0; t < T; t++){
		long long a, b;
		cin>>a>>b;
		
		int bcnt = binsearch(v, a);
		int acnt = binsearch(v, b + 1);
		int ans = acnt - bcnt;		

		cout<<"Case #"<<t + 1<<": "<<ans<<endl;
	}
}