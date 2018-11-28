#include <iostream>
#include <stdio.h>
#include <conio.h>
#include <math.h>
#include <string>

using namespace std;

int main(){
	int t, tt, s, n, sum;
	string r;
	cin>>t;
	tt=0;
	while(tt++ < t){
		n = 0;
		sum = 0;
		cin>>s;
		getline(cin, r);
		r = r.substr(1);
		// cout<<r<<endl;
		for(int i = 0; i<=s; i++){
			if(i > sum){
				n += i-sum;
				sum += i-sum;
			}
			sum += (int)r[i]-48;
			// cout<<sum<<endl;
		}
		cout<<"Case #"<<tt<<": "<<n<<endl;
	}
	return 0;
}