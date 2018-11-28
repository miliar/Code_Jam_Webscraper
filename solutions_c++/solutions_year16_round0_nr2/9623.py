#include <bits/stdc++.h>
using namespace std;

int main() {
	int n;cin>>n;
	for (int i=1;i<=n;i++){
		string x;cin>>x;
		int k=x.length()-1;
		int total=0;
		if (x[k]=='-') total++;
		for (int j=k-1;j>=0;j--){
			if (x[j]!=x[j+1]) total++;
		}
		cout << "Case #" << i << ": " <<total<<endl;
	}
	return 0;
}