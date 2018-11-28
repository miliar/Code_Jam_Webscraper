#include<iostream>
#include<string>
#include<stack>
#include <fstream>
using namespace std;

int main(){
	int t,len;
	ifstream myfile ("A-large.in");
	ofstream myf ("output.txt");
	myfile >> t;
	string s,st;
	char ch;
	for(int j=1;j<t+1;j++){
		myfile>>s;
		stack<char> ta;
		len = s.length();
		st="";
		st+=s[0];
		ch = s[0]; 
		for(int i=1;i<len;i++){
			if(s[i]>=ch){
				ta.push(s[i]);
				ch=s[i]; }
			else
				st+=s[i]; }
			
		myf<<"Case #"<<j<<": ";
		
		while(!ta.empty()){
			myf<<ta.top();
			ta.pop(); }

		myf<<st;
		myf<<"\n";
	}
	myfile.close();
	myf.close();
	return 0;
}
		
