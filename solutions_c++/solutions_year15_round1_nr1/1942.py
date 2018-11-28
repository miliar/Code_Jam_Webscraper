#include <iostream>
#include <string>
#include <vector>
#include <cassert>
using namespace std;

vector<int> make_v(int n){
	vector<int> v;
	int curr;
	for(int i = 0; i<n; i++){
		cin >> curr;
		v.push_back(curr);
	}
	return v;
}

void solve1(vector<int> v){
	int sum = 0;
	for(int i = 0; i<v.size()-1;i++){
		if(v[i] > v[i+1]){
			sum+=v[i]-v[i+1];
		}
	}
	cout << sum << " ";
}

void solve2(vector<int> v){
	int largest_diff = -1;
	for(int i = 0; i<v.size()-1; i++){
		if(v[i] > v[i+1]){
			if(largest_diff == -1 || v[i]-v[i+1] > largest_diff){
				largest_diff = v[i] - v[i+1];
			}
		}
	}
	if(largest_diff==-1)
		largest_diff=0;
	int sum = 0;
	for(int i = 0; i<v.size()-1; i++){
		if(v[i] < largest_diff){
			sum+= v[i];
		}
		else{
			sum+=largest_diff;
		}
	}

	cout << sum;
}
void solve(){
	int num;
	cin >> num;
	vector<int> v;
	v.clear();
	v = make_v(num);
	solve1(v);
	solve2(v);
}

int main(){
	FILE *fin = freopen("large.in", "r", stdin);
	assert( fin != NULL);
	int cases; 
	cin >> cases;
	for(int i = 0; i < cases; i++){
		cout << "Case #" << i+1 <<": ";
		solve();
		cout << endl;
	}
	return 0;
}