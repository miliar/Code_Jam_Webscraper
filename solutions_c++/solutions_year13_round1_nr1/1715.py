#include <iostream>
#include <cmath>
#include <stdio.h>
#include <vector>

using namespace std;

int main(){
	int tst;
	cin>>tst;
	for(int test=1;test<=tst;test++){
		long long int r,t;
		cin>>r>>t;
		long long int num = (2*r)+1;
		int count=0;
		while(t>=num){
			t=t-num;
			num=num+4;
			count++;
		}
		cout<<"Case #"<<test<<": "<<count<<endl;
	}
	return 0;
}