#include<iostream>
#include<fstream>
using namespace std;
int main(){
	int t;
	long long a;
	int s;
	ifstream input;
	ofstream output;
	input.open("cjama.txt");
	output.open("caout.txt");
	input>>t;
	string str;
	int ss=t;
	while(t--){
		input>>s>>str;
		a=str[0]-'0';
		long long ans=0;
		for(int i=1;i<str.size();i++){
			if(a>=i){
				a+=(str[i]-'0');
			}
			else{ 
				
				ans+=(i-a);
				a+=(i-a)+str[i]-'0';
				
			}
		}
		output<<"Case #"<<ss-t<<": "<<ans<<endl;
	}
	return 0;
}
