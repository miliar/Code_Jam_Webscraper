#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		int a;
		cin>>a;
		int b[a+1];
		string x;
		cin>>x;
		int j=0;
		for(j=0;j<=a;j++){
			b[j]=x[j]-'0';
		}
		int sum=b[0],count=0;
		for(j=1;j<=a;j++){
			if(sum<j){
				count++;
				sum++;
			}
			sum+=b[j];
		}
		cout<<"case #"<<i+1<<": "<<count<<endl;
	}
	return 0;
}
