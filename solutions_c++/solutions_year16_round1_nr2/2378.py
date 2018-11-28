#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

void solve(int z){
	int n;
	int a;
	cin >> n;
	vector<int> v;
	vector<int>::iterator it;
	for(int i=0;i<n*2-1;++i){
		for(int j=0;j<n;++j){
			cin >> a;
			it=find(v.begin(),v.end(),a);
			if(it==v.end())
				v.push_back(a);
			else{
				v.erase(it);
			}
		}
	}
	sort(v.begin(),v.end());
	cout << "Case #" << z << ": ";
	for(int i=0;i<v.size();++i)
		cout << v[i] << " ";
	cout << endl;
}

int main(){
	int t;
	cin >> t;
	for(int i=1;i<=t;++i){
		solve(i);
	}
}
/*
1
3
1 2 3
2 3 5
3 5 6
2 3 4
1 2 3
*/