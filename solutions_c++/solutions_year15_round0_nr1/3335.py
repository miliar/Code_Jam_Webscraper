#include<vector>
#include<algorithm>
#include<iostream>
#include<string>
using namespace std;
int main(){
	int T;
	cin>>T;
	int k=1;
	while(k<=T){
		int count=0;
		int S = 0;
		int Smax;
		cin>>Smax;
		vector<int> shyness(Smax+1, 0);
		string s;
		cin>>s;
		for(int i=0; i<=Smax; i++)
			shyness[i] = s[i]-'0';
		for(int i=0; i<=Smax; i++){
			if(shyness[i]==0) continue;
			if(S>=i){
				S+=shyness[i];
				continue;
			}
			count+=i-S;
			S=i+(shyness[i]);
			
		}
		cout<<"Case #"<<k<<": "<<count<<endl;
		k++;
	}
	return 0;
}
