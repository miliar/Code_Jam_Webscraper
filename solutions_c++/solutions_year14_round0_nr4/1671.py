#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int best(vector<double> p1, vector<double> p2)
{
	sort(p1.begin(), p1.end());
	sort(p2.begin(), p2.end());

	int ret = 0;
	int i2 = 0;
	for(int i = 0; i< p1.size(); ++i){
		if(p1[i] > p2[i2]) {
			ret++;
			i2++;
		}
	}
	return ret;
}

int worst(vector<double> p1, vector<double> p2)
{
	sort(p1.begin(), p1.end());
	sort(p2.begin(), p2.end());
	int ret = 0;
	int i2 = 0;
	for(int i = 0; i< p2.size(); ++i){
		if(p2[i] < p1[i2]) {
			ret++;
		}
		else {
			i2 ++;
		}
	}
	return ret;
}


int main()
{
	int T;
	cin >> T;
	for(int k = 1; k<= T; ++k){
		int n;
		cin >> n;
		vector<double> p1 = vector<double>(n);
		vector<double> p2 = vector<double>(n);
		for(int i = 0; i< n; ++i) {
			cin >> p1[i];
		}
		for(int i = 0; i< n; ++i) {
			cin >> p2[i];
		}
		
		int v1 = best(p1, p2);
		int v2 = worst(p1, p2);
		printf("Case #%d: %d %d\n", k, v1, v2);
	}
}

