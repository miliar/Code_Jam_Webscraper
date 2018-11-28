#include<iostream>
#include<fstream>
#include<cstring>
#include<math.h>
#include<sstream>

using namespace std;

//#define SSTR( x ) dynamic_cast< std::ostringstream & >( \
   //     ( std::ostringstream() << std::dec << x ) ).str()

int isPalindrome(int a){
	if(a<10)
		return 1;
	
		ostringstream ss;
		ss << a;
		string num=ss.str();
		int l=num.length();
		for(int i=0;i<l/2;i++){
			if(num[i]!=num[l-i-1])
				return 0;
		}
	 return 1;
}

int isSq(int a){
	int r=sqrt(a);
	if(a==r*r && isPalindrome(r)==1)
		return 1;
	else
		return 0;
}

int main(){
	ifstream in("inp.in");
	ofstream out("out.out");

	int test;
	char nxt[10];
	in>>test;
	in.getline(nxt,10);

	for(int i=0;i<test;i++){
		int a,b,count=0,flag1=-1,flag2=-1;
		in>>a;
		in>>b;
		for(;a<=b;a++){
			flag1=isPalindrome(a);
			flag2=isSq(a);
			/*out<<"\nNew number";
			out<<a;
			out<<flag1;
			out<<flag2;*/
		
		if(flag1==1 && flag2==1)
			count++;
		}

		in.getline(nxt,10);		//CHECK IF IT IS REQ OR NOT

		out<<"Case #";
		out<<i+1;
		out<<": ";
		out<<count;
		//out<<flag1;
		
		out<<"\n";
	}

	in.close();
	out.close();
	return 0;
}