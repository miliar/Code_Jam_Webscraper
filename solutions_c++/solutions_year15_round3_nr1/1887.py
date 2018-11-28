#include<iostream>
#include<vector>
using namespace std;
int process(vector<int> a,int x){
	int r, c, w;
	int p = (x - 1) * 3;
	r = a[p]; 
	c = a[p + 1]; 
	w = a[p + 2];
	int sep;
	if (c%w == 0)
		sep = (c - w) / w;
	else{
		
		sep = (c - (c%w)) / w;
	}
	int tr;
	tr = (sep+w)*r;
	return tr;
}
int main(){
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("output2.out", "w", stdout);
	int t,x;
	cin >> t;
	vector<int> a;
	for (int i = 0; i < t; i++)
		for (int j = 0; j < 3;j++)
	{
		cin >> x;
		a.push_back(x);
	}
	for (int k = 0; k < t; k++){
		cout << "case #" << k + 1 << ": " << process(a, k + 1)<<endl;
	}
	
	return 0;
}