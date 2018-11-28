#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
typedef long long LL;

main() {
	FILE *fin = freopen("in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("out", "w", stdout);
	int T;

	
	cin >> T;
	for(int t = 1; t <= T; t++){
		int n;
		vector<int> a1,a2;
		int c1=0,c2=0;
		int max=0;
		scanf(" %d ", &n);
		for(int j =0; j<n; j++){
			int a;
			scanf(" %d ", &a);
			a1.push_back(a);
			// cout << a << " ";
			if(j>0)
				if(a1[j]<a1[j-1]){
					int temp =(a1[j-1]-a1[j]);
					c1+=temp;
					max = ((max>temp)?max:temp);
				}

		}
		for(int j=0;j< n-1;j++){
			if(a1[j]>=max) c2+=max;
			else c2+=a1[j];
		}

		cout <<"Case #"<<t<<": "<<c1<<" "<<c2<<endl;
	}
	exit(0);
}