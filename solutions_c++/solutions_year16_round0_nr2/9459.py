#include <iostream>
using namespace std;

long recursion(string st, int i){
	if(i==0){
		if(st[i] == '+')
			return 0;
		else
			return 1;
	}
	if(st[i] == '+'){
		return recursion(st,i-1);
	}
	if(st[i] == '-' && st[i-1] == '-'){
		return recursion(st,i-1);
	}
	if(st[i] == '-' && st[i-1] == '+'){
		return 2+recursion(st,i-1);
	}

}

int main() {
	// your code goes here
	int T;
	cin>>T;
	for(int t=0;t<T;t++){
		string st;
		cin>>st;
		cout<<"Case #"<<t+1<<": "<<recursion(st,st.length()-1)<<endl;
		
		
	}

	return 0;
}