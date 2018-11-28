#include<bits/stdc++.h>
using namespace std;
int main() {
	ifstream myfile;
	myfile.open("A-large.in");
	ofstream mm;
	mm.open("op2.txt");
	int t;
	myfile>>t;
	for(int l=1;l<=t;l++){
		long long int n, tmp, j=1;
		myfile>>n;
		if(n==0){
			mm<<"Case #"<<l<<": INSOMNIA\n";
			continue;			
		}
		int c =0, ar[10], i;
		for(i=0;i<10;i++) ar[i]=0;
		while(c<10 && n!=0){
			tmp=j*n;
			while(tmp>0){
				int k = tmp%10;
				if(ar[k]==0) {
					ar[k]=1; 
					//cout<<k<<" ";
					c++;
				}
				tmp=tmp/10;
			}
			j++;
		}
		mm<<"Case #"<<l<<": "<<(n*(j-1))<<endl;
	}
	return 0;
}
