#include <iostream>
#include <unordered_map>
#include <string>
#include <set>
using namespace std;
int foo(int n){
	set<char> st;
	int crt=n;
	for(int i=0;i<100;i++){
		string tmp = to_string(crt);
		//cout<<tmp<<endl;
		for(auto x:tmp){
			st.insert(x);
		}
		if(st.size()==10)return crt;
		crt=n*(i+2);
		// cout<<"size: "<<st.size()<<endl;
	}
	return -1;
}
int main(){
	int T,n;
	cin>>T;
	int x=0;
	while(T--){
		cin>>n;
		x++;
		int ret = foo(n);
		if(ret==-1){
			cout << "Case #"<<x<<": INSOMNIA"<<endl;
		} else {
			cout << "Case #"<<x<<": "<<ret<<endl;
		}

	}
	return 0;
}
