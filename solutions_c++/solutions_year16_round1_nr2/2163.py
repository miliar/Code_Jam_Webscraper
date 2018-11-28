#include <bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	ios_base::sync_with_stdio(0);
	int t,i,j=1,n,s,k;
	int a[6000];
	ifstream infile;
	ofstream outfile;
	infile.open("B-large.in");
	outfile.open("output1.txt");
	infile>>t;
	while(t--){
		infile>>n;
		vector<int> b;
		s=(2*n-1)*n;
		for(i=0;i<s;i++)
		infile>>a[i];
		sort(a,a+s);
		a[s]=3000;
		for(i=0;i<s;i++){
			if(a[i]==a[i+1]) i++;
			else b.push_back(a[i]);
		}
		sort(b.begin(),b.end());
		outfile<<"Case #"<<j<<": ";
		for(i=0;i<n;i++)
		outfile<<b[i]<<" ";
		outfile<<endl;
		j++;
	}
	return 0;
}
