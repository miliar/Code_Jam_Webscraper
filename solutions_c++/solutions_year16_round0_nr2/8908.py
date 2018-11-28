#include <iostream>
#include <fstream>
#include <string>
#include <stack>
using namespace std;

void stringtostack(stack<char>& mystack,string s) {
	int len=s.length();
	for (int i=len-1;i>=0l;i--) {
		mystack.push(s[i]);
	}
}
unsigned int makehappy(stack<char> mystack)
 {
	unsigned int count=0;
	stack<char> tempst;
	char topelem;
	while(1)
{
	do
	{ 	topelem=mystack.top();
		mystack.pop();
		tempst.push(topelem);
		if(mystack.empty()) 
		{
			if(topelem=='+') return count;
			else return (count +1) ;	
		}
	} while(mystack.top()==topelem);
	// flip now
	count++;
	stack<char> tempst2;
	while(!tempst.empty()) 
	{
		tempst2.push(tempst.top());
		tempst.pop();
	}
	while(!tempst2.empty()) 
	{ char tempelm=tempst2.top();
		tempst2.pop();
		if(tempelm=='+') mystack.push('-');
		else mystack.push('+');
	}
}
}
int main() {
	ifstream infile;
	infile.open("input.txt");
	ofstream outfile;
	outfile.open("output.txt");
	string S;
	unsigned int T;
	infile>>T;
	for(int i=1;i<=T;i++) {
		stack<char> mystack;
		infile>>S;
		stringtostack(mystack,S);
	unsigned int count=0;
	count= makehappy(mystack);
outfile<<"Case #"<<i<<": "<<count<<endl;
}
}
