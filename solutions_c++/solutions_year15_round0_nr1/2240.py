#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int j=1; j<=t; j++){
		int sm;
		cin>>sm;
		vector<int> a(sm+1);
		string s;
		cin>>s;
		for(int i=0; i<=sm; i++){
			a[i] = s[i] - '0';
		}
		int sum=0, m=0;
		for(int i=0; i<=sm; i++){
			if(a[i] != 0){
				if(sum + m < i) m = i - sum;
				sum = sum + a[i];
			}
		}
		cout<<"Case #"<<j<<": "<<m<<endl;
	}
	return 0;
}
