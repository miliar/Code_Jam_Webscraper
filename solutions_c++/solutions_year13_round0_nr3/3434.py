#include<iostream>
#include<fstream>
#include<string>
#include<math.h>
#include<sstream>

using namespace std;

bool isFair(int x){
	string s;
	stringstream ss;
	ss<<x;
	ss>>s;
	for(int i=0;i<=(s.length()-1)/2;i++){
		if(s.at(i)!=s.at(s.length()-1-i)){
			return false;
		}
	}
	return true;
}
bool isS(int x){
	int s=sqrt(x);
	if(x==s*s)
		return true;
	else 
		return false;
}

int mfind(int a,int b){
	int r=0;
	for(int i=a;i<=b;i++){
		if(isFair(i)&&isS(i))
			if(isFair(sqrt(i)))
				r++;
	}
	return r;
}


void main(){
	ifstream f1("D:\\codeJam\\C\\C-small-attempt1.in");
	ofstream f2("D:\\codeJam\\C\\C-small-attempt1.out");
	int T;
	f1>>T;
	for(int t=0;t<T;t++){
		int A,B;
		f1>>A>>B;
		int r=mfind(A,B);
		f2<<"Case #"<<t+1<<": "<<r<<endl;
	}
	f1.close();
	f2.close();
}
