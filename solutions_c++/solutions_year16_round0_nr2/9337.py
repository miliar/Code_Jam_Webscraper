#include<iostream>
using namespace std;
int main(){
	int T;
	cin>>T;
	int i;
	for(i=0;i<T;i++){
		string inp;
		cin>>inp;
		int inpSize = inp.length();
		int j,ans=0;
		char firstc = inp[0];
		for(j=0; j<inpSize;j++){
			if(inp[j] == firstc)
				continue;
			else{
				firstc = inp[j];
				ans++;
			}
		
		}
		if(firstc == '-'){
			ans++;
		}
		cout<<"Case #"<<(i+1)<<": "<<ans<<endl;
	}
	return 0;
}
