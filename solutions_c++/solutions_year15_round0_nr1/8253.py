#include <iostream>
using namespace std;

string s;
int n,d,sum,out;

int main(){
	cin>>n;
	for(int i=0;i<n;i++){
		cin>>d>>s;
		sum=out=0;
		for(int j=0;j<=d;j++){
			if(sum<j){ 
				out+=j-sum;
				sum+=j-sum;
			}
			sum+=s[j]-'0';
		}
		cout<<"Case #"<<i+1<<": "<<out<<endl;
	}
	return 0;
}
