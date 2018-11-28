#include<iostream>
#include<fstream>
#include<cstdlib>
using namespace std;
class sol{
public:
	int minflip(string& str,int end){
		if(end==0)
			return str[0]=='-';
		for(int i=end;i>=0;i--){
			if(str[i]=='-')
				return 1+changetoneg(str,i-1);
		}
		return 0;
	}
	int changetoneg(string& str,int end){
		if(end==0)
			return str[0]=='+';
		for(int i=end;i>=0;i--){
			if(str[i]=='+')
				return 1+minflip(str,i-1);
		}
		return 0;
	}
};
int main(){
	ifstream is("B-large.in");
	ofstream os("Output.txt");
	sol s;
	int num;
	is>>num;
	string str;
	int result;
	for(int i=1;i<=num;i++){
		is>>str;
		result=s.minflip(str,str.size()-1);
		os<<"Case #"<<i<<": "<<result<<"\n";
	}
	is.close();
	os.close();
}