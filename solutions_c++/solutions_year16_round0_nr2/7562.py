#include "iostream"
#include <string> 
#include <algorithm>


using namespace std;
bool state(char c){
	if(c=='+')return true;
	return false;
}
void flip(string &s,int at){
	string n=s.substr(0,at);
	reverse(n.begin(), n.end());
	for(int i=0;i<n.length();i++){
		if(state(n.at(i))){
			n.at(i)='-';
		}else{
			n.at(i)='+';
		}
	}
	s.replace(0,at,n);
}
int getMin(string s){
	int N=0;
	bool lastOne=state(s.at(0));
	for(int p=0;p<s.length();p++){
		if(state(s.at(p))!=lastOne){
			flip(s,p);
			N++;
		}
		lastOne=state(s.at(p));
	}
	if(!state(s.at(0)))N++;
	return N;
}
int main(){
	int T;
	cin>>T;
	if(T<0||T>100){return 0;}

	for(int i=1;i<=T;i++){
	string s;
	cin>>s;
	//getline (std::cin,s);
	int r=getMin(s);
	cout<<"Case #"<<i<<": "<<r<<endl;
	}
	return 0;
}