#include <bits/stdc++.h>
using namespace std;

int main () {
	ios_base::sync_with_stdio(false);
	int t;
	cin >> t;
	int k =0;
	while (t--) {
		//int k = 0;
		int n;
		cin >> n;
		string str;
		cin >> str;
		int sum = 0;
		int temp = 0;
		int reqrd = 0;
		for (int i = 0; i <= n; i++ ) {
			temp = str[i] - 48;
			if (temp != 0 && i > sum){
				reqrd += i - sum;
				sum = sum + reqrd;
			}
			//cout <<reqrd<<"**"<<endl;
			sum += temp;
		}
		//cout <<sum<<endl;
		cout <<"Case #"<<++k<<": "<<reqrd<<endl;
	}

}
