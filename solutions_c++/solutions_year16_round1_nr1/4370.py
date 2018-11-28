#include<iostream>
#include<deque>
#include<fstream>
#include<string>

using namespace std;
int main(){
	int t,i=1;
	string str;
	ifstream inf("C:\\Users\\shyam gupta\\Downloads\\A-large.in");
	ofstream outf;
	outf.open("C:\\Users\\shyam gupta\\\Downloads\\output.txt");
	inf>>t;
	getline(inf,str);
	deque<char> q;
	while(t--){
		str.clear();
		getline(inf,str);
		char b=str[0];
		for(int j=0;j<str.length();j++){
			if((int)b>(int)str[j]){
			q.push_back(str[j]);
			cout<<str[j];
		}
			else{
			q.push_front(str[j]);
			b=str[j];
		}
		}
		cout<<endl;
		outf<<"Case #"<<i<<": ";
		while(!q.empty()){
			outf<<q.front();
			q.pop_front();
		}
		outf<<endl;
		++i;
	}
	inf.close();
	outf.close();
	return 0;
}
