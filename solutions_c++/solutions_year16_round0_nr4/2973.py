//Naman Agarwal
//IIT Mandi
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <iomanip>
#include <string>

using namespace std;

#define lli long long int

int main() {
	ios::sync_with_stdio(false);
	int t,tc=1;
	cin>>t;
	while(t--){
		lli k,c,s;
		cin>>k>>c>>s;
		cout<<"Case #"<<tc<<": ";
		for(int i=1;i<k;i++){
			cout<<i<<" ";
		}
		cout<<k<<"\n";
		tc++;
	}
	return 0;
}