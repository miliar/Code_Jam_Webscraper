#include<iostream>
#include<string>
#include<cstdio>
#include<cstdlib>
#include<fstream>

using namespace std;

int getResult(string str, int n);
inline int isMo (char ch);

int main(){

	ifstream fin("A-small-attempt0.in");
	ofstream out("A-small-attempt0.out");

	int n, howMany;
	string str;

	fin>>howMany;
	for(int k=0; k<howMany;k++){
		fin>>str>>n;
		
		cout<<"Case #"<<(k+1)<<": "<<getResult(str, n)<<endl;
		out<<"Case #"<<(k+1)<<": "<<getResult(str, n)<<endl;
	}
	fin.close();
	out.close();


	return 0;
}

int getResult(string str, int n){
	int count=0;
	int tmpc=0;

	int length;
	length = str.length();
	for(int i=0;i<length; i++){
		tmpc=0;
		for(int j=i;j<length;j++){
			if(isMo(str[j]))
				tmpc++;
			else
				tmpc=0;
			if(tmpc>=n){
				count+=(length-j);
				break;
			}
		}
	}

	return count;
}

inline int isMo(char ch){
	if(ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u')
		return 0;
	else
		return 1;
}