#include <iostream>
#include <set>
#include <sstream>
using namespace std;
string toString(long long int a){
	ostringstream ss;
	ss<<a;
	return ss.str();
}
int main(){
	int n;
	cin>>n;
	//n=1000000;
	for(int case_num=1;case_num<=n;case_num++){
		long long int N;
		cin>>N;
		//N=case_num;
		if(N==0){
			cout<<"Case #"<<case_num<<": "<<"INSOMNIA"<<endl;
			continue;
		}
		long long int a=N;
		long long int ans;
		set<char> s;
		for(long long int i=1;s.size()<10;i++){
			a = i*N;
			if(a>10000000000000L){
				cout<<"Overflow ";
				return 0;
			}
			ans = a;
			string b = toString(a);
			for(int j=0;j<b.length();j++)
				s.insert(b[j]);
		}
		cout<<"Case #"<<case_num<<": "<<ans<<endl;
	}
}