//Dedicato a Claudia,
//ti voglio bene.

#include <iostream>
#include <string>

using namespace std;

int solve(string pcakes){
	//cout<<pcakes<<" ";
	int found=pcakes.rfind('-');
	if(found==string::npos)return 0;
	for(int i=0;i<=found;i++)pcakes[i]=pcakes[i]=='-'?'+':'-';
	//cout<<pcakes<<endl;
	return 1+solve(pcakes);
}

int main(){
	int T;
	string pcs;
	cin>>T;
	getline(cin,pcs);
	for(int t=1;t<=T;t++){
		getline(cin,pcs);
		cout<<"Case #"<<t<<": "<<solve(pcs)<<endl;
	}
	return 0;
}
