#include<bits/stdc++.h>
using namespace std;

int main(){
	int T;
	cin>>T;
	
	for(int k=1; k<=T; k++){
		cout<<"Case #"<<k<<": ";
		int n;
		cin>>n;
		if(n==0){
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		int i=1;
		set<int> digits;
		while(true){
			int r = i*n;
			while(r>0){
				digits.insert(r%10);
				r/=10;
			}
			if(digits.size()==10) break;
			i++;
		}
		cout<<i*n<<endl;
	}
	return 0;
}
