#include<iostream>
#include<vector>
using namespace std;
void print(vector<int>& a){
	for(int i = a.size()-1; i >=0; i --) cout<<a[i]; cout<<endl;
}
int main (){
	int cases = 0 ;
	cin >> cases;
	int output_case = 1;
	while( cases --){
		cout<<"Case #"<<(output_case++)<<": ";
		int x ; 
		cin >> x;
		if(x== 0) {
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		vector<int> v,a;
		while(x){
			v.push_back(x%10);
			x/=10;
		}
		//print(v);
		
		a = v;
		int req = 0 , mask = 0; for(int i =0 ; i <10; i ++) req|=(1<<i);
		for(int i =0 ; i <a.size(); i ++) mask |= 1<<a[i];
		if(mask == req) {
			print(a);
			continue;
		}

		while(1){
			int carry = 0 ;
			for(int i =0 ; i<a.size(); i ++){
				int sum = a[i] + carry;
				if( i < v.size() ) sum += v[i];
				a[i] = sum %10;
				carry = sum/10;
				mask|=1<<a[i];
			}	
			if(carry) {
				a.push_back(carry);
				mask|= 1<<carry;
			}
			//print(a);
			if(mask == req){
				print(a);
				break;
			}
		}
	}
}
