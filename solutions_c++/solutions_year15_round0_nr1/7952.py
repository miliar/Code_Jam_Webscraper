#include <iostream>
#include <string>
using namespace std;
int main(){
	int t;
	cin>>t;
			
	int cnt=1;
	while(cnt<=t){
		int shymax;
		cin>>shymax;
		string a;
		cin>>a;
		int shy[shymax+1];
		
		for(int i=0; i<= shymax;i++) shy[i] = a[i]-'0';
		
		int ppl = shy[0], req=0;		//req = required number of extras ; ppl = number of people with me including the ones i call
		
		cout<<"Case #"<<cnt<<": ";
		
		for(int i=1; i<= shymax;i++){
			int n = max ( 0 , i-ppl);
			req += n;
			ppl += shy[i] + n;
		}
		
		cout<<req<<endl;
		cnt++;
	}
	return 0;
}
