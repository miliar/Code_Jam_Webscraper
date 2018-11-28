#include<iostream>
#include<vector>
using namespace std;


int main() {
	int t,cs = 1;
	cin>>t;
	while(t--) {
		cout<<"Case #"<<cs++<<": ";
		int n;
		cin>>n;
		vector<int> v(n);
		vector<char> c(n);
		for(int i=0;i<n;i++) cin>>v[i];
		for(int i=0;i<n;i++) c[i] = i+'A';

		while(v.size() > 2) {
			int len = v.size();
			int max = -1;
			int pos = -1;
			for(int i=0;i<len;i++) {
				if(v[i] > max) {
					max = v[i];
					pos = i;
				}
			}

			cout<<c[pos]<<" ";
			v[pos] -= 1;
			if(v[pos] == 0) {
				v.erase(v.begin()+pos);
				c.erase(c.begin()+pos);
			}


		}

		while(v[0]) {
			cout<<c[0]<<c[1]<<" ";
			v[0] -= 1;
			v[1] -= 1;
		}
		cout<<endl;
	}
	
	return 0;
}