#include<iostream>
#include<fstream>
#include<cstring>
#include<math.h>
#include<sstream>

using namespace std;

int main(){
	ifstream in("inp.in");
	ofstream out("out.out");

	long int test,r,t,c=1;
	char nxt[10];
	in>>test;
	in.getline(nxt,10);
	while(test-->0){
		in>>r;
		in>>t;
		//rest=t;
		int count=-1;
		while(t>=0){
			/*out<<t;
			out<<" ";*/
			t = t-(2*r+1);
			r=r+2;
			count++;
			
		}
		out<<"Case #";
		out<<c;
		out<<": ";
		out<<count;
		out<<"\n";
		c++;
	}

	in.close();
	out.close();
	return 0;
}