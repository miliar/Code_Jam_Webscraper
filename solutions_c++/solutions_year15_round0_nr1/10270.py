#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main(){
	std::ios::sync_with_stdio(false);
	ofstream writer("file1.txt");
	ifstream reader("A-small-attempt0.in");
	int t,smax,x,min,temp,j=1;
	string s;
	//cin>>t;
	if(reader.is_open()){
		reader>>t;
	}
	while(t--){
		min=0;
		//cin>>smax>>s;
		if(reader.is_open()){
		reader>>smax>>s;
	}
		temp=0;
		for(int i=0;i<smax;i++){
			temp+=int(s[i])-48;
			if(temp<i+1 && int(s[i+1])!=48){
				min=min+(i+1)-temp;
				temp=temp+min;
			}
		}
		if(writer.is_open()){
		writer<<"Case #"<<j<<": "<<min<<endl;
		}
		j++;
	}
	reader.close();
	writer.close();
}