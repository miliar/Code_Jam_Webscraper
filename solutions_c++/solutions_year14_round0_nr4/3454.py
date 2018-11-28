#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

int main(){
	freopen("input", "r", stdin);
	freopen("output", "w", stdout);
	int t;
	cin>>t;
	for(int p = 0; p < t; p++){
		int n;
		cin>>n;
		vector<double> a, b;
		for(int i = 0; i < n; i++){
			double c;
			cin>>c;
			a.push_back(c);
		}
		for(int i = 0; i < n; i++){
			double c;
			cin>>c;
			b.push_back(c);
		}
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());
		int first = 0, second = 0;
		int beg = 0;
		for(int i = 0; i < a.size(); i++){
			while(beg < a.size()){
				if(a[beg++] > b[i]){
					first++;
					break;
				}
			}
		}
		beg = 0;
		for(int i = 0; i < a.size(); i++){
			while(beg < a.size()){
				if(b[beg++] > a[i]){
					second++;
					break;
				}
			}
		}
		cout<<"Case #"<<p + 1<<": "<<first<<" "<<(n - second)<<endl;
	}
	return 0;
}