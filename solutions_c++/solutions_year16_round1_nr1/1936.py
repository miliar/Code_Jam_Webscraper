#include <iostream>
#include <list>
#include <vector>
#include<fstream>
using namespace std;

int main() {
	// your code goes here
	ofstream out;
	out.open("1b.out");
	ifstream in;
	in.open("1b.in");
	int t,i;
	in>>t;
	for(int j=1;j<=t;j++){
		string str;
		char l,r; 
		in>>str;
		list<int> v;
		v.push_back(0);
		l=str[0];r=str[0];
		for(i=1;i<str.length();i++){
			if(str[i]>=l){
				v.push_front(i);
				l=str[i];
			}
			else //(str[i]<=r){
			{	v.push_back(i);
				r=str[i];
			}
			/*else{
				if(str[i]-r > l-str[i])
					v.push_front(i);
				else
					v.push_back(i);
			}*/
			
		}
		out<<"Case #"<<j<<": ";
		for (std::list<int>::iterator it=v.begin(); it != v.end(); ++it)
    	{	out<< str[*it];}
    	out<<"\n";
	}
	return 0;
}
