#include<iostream>
using namespace std;
 
int main() {
	int T,Smax,k=1;
	cin>>T;
	char str[1002];
	while(T--) {
		int count=0,sum=0;
		cin>>Smax>>str;
		int j=0;
		while(str[j]) {
			if(sum >= j) {
				sum = sum + (str[j] - '0');
			}
			else {
				sum = j + (str[j] - '0');
				count++;
			}
			j++;
		}
		cout<<"Case #"<<k<<": "<<count<<endl;
		k++;
	}
	return 0;
}