#include <iostream>
using namespace std;
#define loop(j,begin,end) for(int j=begin;j<=end;j++)

int main(){
	int t,i=0;
	int k,c,s;
	
	cin>>t;
	while(i++ < t){
		cin>>k>>c>>s;
		cout<<"Case #"<<i<<":";
		if(k==s){
			loop(j,1,k){
				cout<<" "<<j;
			}
		}else{
			cout<<" 0";
		}
		cout<<endl;
	}
	return 0;
}