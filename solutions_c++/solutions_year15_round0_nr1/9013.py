#include <iostream>
using namespace std;

int main(){
	int T;
	cin>>T;
	for(int test=1;test<=T;test++){
		int smax;
		int shyness[1001];
		string shy;
		cin>>smax;
		cin>>shy;
		for(int i=0;i<=smax;i++){
			shyness[i]=shy[i]-'0';
		}
		int curr=shyness[0];
		int invite=0;
		int total_invite=0;
		for(int i=1;i<=smax;i++){
			invite=0;
			if(i>curr && shyness[i]!=0){
				invite = i-curr;
				total_invite+=invite;
			}
			curr+=shyness[i]+invite;
		}
		cout<<"Case #"<<test<<": "<<total_invite<<endl;
	}
}