#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main(){
	int t,i=1;
	unsigned long long int ans=0;
	bool b=0;
	string str;
	ifstream inf("C:\\Users\\shyam gupta\\Downloads\\B-large.in");
	ofstream outf;
	outf.open("C:\\Users\\shyam gupta\\\Downloads\\output.txt");
	inf>>t;
	getline(inf,str);
	str.clear();
	while(t--){
		getline(inf,str);
		ans=0;
		if(str[0]=='-')
		b=0;
		else
		b=1;
		outf<<"Case #"<<i<<":"<<" ";
		for(int j=1;j<str.length();j++){
			if(b){
				if(str[j]=='-'){
				++ans;
				b=0;
			}
			}
			else{
				if(str[j]=='+'){
				++ans;
				b=1;
			}
			}
		}
		if(b==0)
		++ans;
		outf<<ans<<endl;
		++i;
	}
	inf.close();
	outf.close();
}
