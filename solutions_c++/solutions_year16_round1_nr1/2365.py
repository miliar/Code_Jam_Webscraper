#include<iostream>
#include<algorithm>
#include<deque>
#include<string>
using namespace std;
string func(string str){
	deque<char> d;
	for(int i=0;i<str.size();i++){
		if(d.size()==0){
			d.push_back(str[i]);
		}else{
			if(str[i]>=d.front()){
				d.push_front(str[i]);
			}else{
				d.push_back(str[i]);
			}
		}
	}
	string output="";
	for(int i=0;i<d.size();i++){
		output.push_back(d[i]);
		
	}
	return output;
}
int main (){
	int x;
	cin>>x;
	string str;
	for(int i=1;i<=x;i++){
		cin>>str;
		cout<<"Case #"<<i<<": "<<func(str)<<endl;
	}
}
