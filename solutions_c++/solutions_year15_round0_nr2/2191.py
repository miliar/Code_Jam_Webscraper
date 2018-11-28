#include <bits/stdc++.h>

using namespace std;

int sq(int y){
	int yy = sqrt(y);
	if(yy*yy == y) return yy;
	else return yy+1;
}


int main(){
	int t;
	cin>>t;
	for(int j=1; j<=t; j++){
		int d;
		cin>>d;
		vector<int> a(d);
		vector<int> p(1003, 0);
		for(int i=0;i<d;i++){
			cin>>a[i];
		}
		int m = 10000;
		for(int i=1;i<1001;i++){
			int sum = 0;
			for(int k=0;k<a.size();k++){
				if(a[k] % i == 0) sum = sum + a[k]/i - 1;
				else{
					double ii = i;
					sum = sum + ceil(a[k]/ii) - 1;
				}
			}
			if(m > sum+i) m = sum+i;
		}
		cout<<"Case #"<<j<<": "<<m<<endl;
	}
}	