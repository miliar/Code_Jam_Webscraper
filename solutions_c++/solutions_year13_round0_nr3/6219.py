#include <iostream>
#include <math.h>
#include <string>
using namespace std;

int main(){
	string s, reverse,root, rRoot;
	int testCases=0;;
	cin>>testCases;
	for(int t=1;t<=testCases;t++) {
		int a,b,k=0,j=2,result=0;
		long double i=1;
		cin>>a>>b;
		while(i<=b){
			i=i+k;
			k=2*j-1;
			j++;
			if(i>=a && i<=b){
				s = to_string(i);
				reverse = string(s.rbegin(), s.rend());
				if(reverse==s) {
					long double r=sqrt(i);
					root = to_string(r);
					rRoot = string(root.rbegin(), root.rend());
					if(rRoot == root) {
						//cout<<"Root "<<root<<' ';
						result++;
					}
				}
			
			}

		}
		cout<<"Case #"<<t<<": "<<result<<endl;
	}
}