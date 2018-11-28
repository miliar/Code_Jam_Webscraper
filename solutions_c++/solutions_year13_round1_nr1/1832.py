#include <iostream>
#include <vector>
#include <cstring>
#include <string>
#include <list>
#include <algorithm>
#include <cmath>

using namespace std;

int main(){
	int t,C;
	cin>>t;
	C = 0;
	while(t--){
		C++;
		long long int r,t;
		cin>>r>>t;
	//	vector<int>v(2010);
		long long int a = r;
		long long int sum = 0,flag = 0;
		for(long long int i = 0;i < 1010;i++){
			sum = sum + (a+1)*(a+1) - (a)*(a);
//			cout<<sum<<endl;
			a = a+2;
			if(sum > t){
				flag = i;
				break;
			}
		}
		cout<<"Case #"<<C<<": "<<flag<<endl;
	}
	return 0;
}