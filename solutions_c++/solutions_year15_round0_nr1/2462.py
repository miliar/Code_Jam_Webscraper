#include<iostream>
using namespace std;

int t,s,act,res;
string k;	
	
int main(){
	cin>>t;
	
	for(int i = 0; i < t; i++){
		cin>>s>>k;
		act = 0;
		res = 0;
		for(int j = 0; j <= s; j++){
			if(act < j){
				res += (j-act);
				act = j;
			}	
			act += (k[j] - '0');
		}
		cout<<"Case #"<<i+1<<": "<<res<<endl;
	}

return 0;
}
