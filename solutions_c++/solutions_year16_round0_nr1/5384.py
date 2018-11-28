#include<bits/stdc++.h>
using namespace std;

int main(){
	int T;cin>>T;
	for(int t=1;t<=T;t++){
		set<int> digits;
		for(int i=0;i<10;i++)
			digits.insert(i);
		set<int> myset;
		int N,n;cin>>N;
		n=N;
		int i=2;
		while(!digits.empty()){
			myset.insert(n);
			int x=n;
			while(x>0){
				if(digits.find(x%10)!=myset.end())
					digits.erase(x%10);
				x/=10;
			}
			if(digits.empty()){
				cout<<"case #"<<t<<": "<<n<<endl;
				break;
			}
			n=i*N;
			i++;
			if(myset.find(n)!=myset.end()){
				cout<<"case #"<<t<<": "<<"INSOMNIA\n";
				break;
			}
		}
	}
}