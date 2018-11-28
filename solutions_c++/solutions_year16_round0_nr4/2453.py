#include<bits/stdc++.h>
using namespace std;
int main() {
	ifstream oo;
	oo.open("D-small-attempt0.in");
	ofstream mm;
	mm.open("op7.txt");
	
	int t,i,k;
	oo>>t;
	for(i=1;i<=t;i++){
		int k,c,s;
		oo>>k>>c>>s;
		if(k==s){
			mm<<"Case #"<<i<<": ";
			for(int j=0;j<k;j++){
				mm<<j+1<<" ";
			}
			mm<<endl;
		}
	}
	return 0;
}
