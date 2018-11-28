#include <iostream>
#include <string>
#include <sstream>
#include <cmath>
using namespace std;
bool is_palindrom(int);
int main(){
	int T;
	cin>>T;
	for (int t=0;t<T;t++){
		int A,B,a,b,count;
		cin>>A>>B;
		a=sqrt(A);
		b=sqrt(B)+1;
		count=0;
		for (int i=a;i<=b;i++)
			if (i*i>=A && i*i<=B && is_palindrom(i) && is_palindrom(i*i))
				count++;
		cout<<"Case #"<<t+1<<": "<<count<<endl;
	}
}
bool is_palindrom(int x){
	ostringstream strm;
	strm << x;
	string s = strm.str();
	for (int i=0,j=s.size()-1;i<j;i++,j--)
		if(s[i]!=s[j])
			return false;
	return true;
}