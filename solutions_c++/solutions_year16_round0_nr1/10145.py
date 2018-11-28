#include <bits/stdc++.h>
using namespace std;
bool seen[10];

int main(){
	long long T,N,c,cc,var,var2;
	bool possible;
	cin >> T;	
	for (int qw=0;qw<T;qw++){
		c=1;
		cc=0;
		possible =true;
		for (int i=0;i<10;++i)seen[i]=false;
		cin >> N;
		if (N==0) possible = false;
		cc=0;
		while (cc<10 && possible){
			var2 = N * c;
			var = var2;
			while (var){
				if (!seen[var%10]++){
				 	cc++;
				}
				var/=10;
			}
			c++;
			}
		cout << "Case #" <<qw+1 << ": ";
		possible? cout << var2 << endl: cout << "INSOMNIA" << endl;
	}
	return 0;
}
