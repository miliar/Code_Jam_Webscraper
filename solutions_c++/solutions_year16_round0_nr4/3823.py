#include <bits/stdc++.h>

using namespace std;

int main()
{
	int t;
	cin>>t;
	for (int count=0; count<t; count++){
		printf("Case #%d: ", count+1);
		int k, c, s;
		cin>>k>>c>>s;
		unsigned long long int step = pow(k, c-1); 
		for (int i=0; i<k; i++){
			cout<<i*step + 1;
			if (i!=k-1) cout<<" ";
		}
		cout<<endl;
	}
	return 0;
}