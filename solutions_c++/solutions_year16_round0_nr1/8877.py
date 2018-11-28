#include<bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	for ( int k=1;k<=t;k++ ){
        int n;
        cin>>n;
        if ( n==0 ) {
			cout<<"Case #"<<k<<": INSOMNIA\n";
        }
        else {
			//vector<bool> digits(10,false);
			set<int> digits;
			int i=0;
			while ( digits.size()!=10 ) {
				i++;
				int num=n*i;
				while ( num>0 ) {
					int r=num%10;
					digits.insert(r);
					num=num/10;
				}
			}
			cout<<"Case #"<<k<<": "<<n*i<<"\n";
		}
	}
	return 0;
}
