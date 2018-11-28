#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main(){
	ofstream fout("outputs.out");
	ifstream fin("input1.in");
	int t,cas;
	fin>>t;
	cas=0;
	while(t--){
		int max,n=0,sum=0,a=0;
		string digit;
		fin>>max>>digit;
		//if(digit[0]=='0') n=1;
		sum=digit[0]-'0';
		for(int i=1;i<=max;i++){
			if(sum>=i){
				sum+=digit[i]-'0';
				//cout<<"sum "<<sum<<endl;
			}
			else{
				n+=(i-sum);
				//cout<<"n "<<n<<endl;
				a=i-sum;
				sum+=digit[i]-'0';
				sum+=a;
				//cout<<"sum "<<sum<<endl;
			}
		}
		fout<<"Case #"<<++cas<<": "<<n<<endl;
	}
}
