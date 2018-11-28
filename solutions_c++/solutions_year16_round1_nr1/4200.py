#include <iostream>
#include<fstream>
#include<string>
#include<stack>
using namespace std;
 
int main() {
 int t,j,le;
 ifstream myfile("A-large.in");
 myfile>>t;
 ofstream p("output.txt");
 string a,b;
 
 for(j=0;j<t;j++)
	{   myfile>>a;
		stack<char> st;
		le = a.length();
		b="";
		b+=a[0];
		
		for(int i=1;i<le;i++){
			if(a[i]>=a[0]){
				st.push(a[i]);
				a[0]=a[i];
			}
			else
				b+=a[i];
		}
	    
		p<<"Case #"<<j+1<<": ";
		
		while(!st.empty()){
			p<<st.top();
			st.pop();
		}
		p<<b<<"\n";
	}
	myfile.close();
	p.close();
	return 0;
}